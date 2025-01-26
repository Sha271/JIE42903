import numpy as np
import matplotlib.pyplot as plt
import random

class JobShop:
    def __init__(self, num_jobs, num_machines, processing_times):
        self.num_jobs = num_jobs
        self.num_machines = num_machines
        self.processing_times = processing_times
        self.schedule = None

    def calculate_makespan(self, schedule):
        job_end_times = [0] * self.num_jobs
        machine_end_times = [0] * self.num_machines

        for job, machine in schedule:
            start_time = max(job_end_times[job], machine_end_times[machine])
            end_time = start_time + self.processing_times[job][machine]
            job_end_times[job] = end_time
            machine_end_times[machine] = end_time

        return max(job_end_times)

    def random_schedule(self):
        schedule = []
        for job in range(self.num_jobs):
            for machine in range(self.num_machines):
                schedule.append((job, machine))
        random.shuffle(schedule)
        return schedule


class Ant:
    def __init__(self, problem, alpha=1, beta=2):
        self.problem = problem
        self.alpha = alpha
        self.beta = beta
        self.tour = []
        self.makespan = float('inf')

    def build_tour(self, pheromone, heuristic):
        unvisited = set((job, machine) for job in range(self.problem.num_jobs) for machine in range(self.problem.num_machines))
        self.tour = []

        while unvisited:
            probabilities = []
            for job, machine in unvisited:
                pher = pheromone[job][machine]
                heu = heuristic[job][machine]
                probabilities.append((job, machine, (pher ** self.alpha) * (heu ** self.beta)))

            total_prob = sum(prob for _, _, prob in probabilities)
            probabilities = [(job, machine, prob / total_prob) for job, machine, prob in probabilities]

            job, machine, _ = random.choices(probabilities, weights=[p[2] for p in probabilities])[0]
            self.tour.append((job, machine))
            unvisited.remove((job, machine))

        self.makespan = self.problem.calculate_makespan(self.tour)


class ACO:
    def __init__(self, problem, num_ants, iterations, alpha=1, beta=2, evaporation_rate=0.5, initial_pheromone=1):
        self.problem = problem
        self.num_ants = num_ants
        self.iterations = iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.initial_pheromone = initial_pheromone

    def run(self):
        pheromone = np.full((self.problem.num_jobs, self.problem.num_machines), self.initial_pheromone)
        heuristic = 1 / (self.problem.processing_times + 1e-10)

        best_tour = None
        best_makespan = float('inf')

        for iteration in range(self.iterations):
            ants = [Ant(self.problem, self.alpha, self.beta) for _ in range(self.num_ants)]
            for ant in ants:
                ant.build_tour(pheromone, heuristic)

                if ant.makespan < best_makespan:
                    best_makespan = ant.makespan
                    best_tour = ant.tour

            pheromone *= (1 - self.evaporation_rate)
            for ant in ants:
                for job, machine in ant.tour:
                    pheromone[job][machine] += 1 / ant.makespan

            print(f"Iteration {iteration + 1}: Best Makespan = {best_makespan}")

        return best_tour, best_makespan


def plot_gantt_chart(schedule, processing_times):
    job_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink']
    fig, ax = plt.subplots(figsize=(10, 6))

    for job, machine in schedule:
        start_time = 0
        for m in range(machine):
            start_time += processing_times[job][m]

        duration = processing_times[job][machine]
        ax.barh(job, duration, left=start_time, color=job_colors[job % len(job_colors)], edgecolor='black')

    ax.set_xlabel("Time")
    ax.set_ylabel("Jobs")
    ax.set_title("Job Shop Scheduling - Gantt Chart")
    ax.set_yticks(range(len(schedule)))
    ax.grid(True)
    plt.show()


# Problem Setup
num_jobs = 4
num_machines = 3
processing_times = np.array([
    [2, 3, 2],
    [1, 2, 3],
    [2, 1, 4],
    [4, 3, 2]
])

# Initialize the Job Shop Problem
problem = JobShop(num_jobs, num_machines, processing_times)

# Run ACO
aco = ACO(problem, num_ants=10, iterations=20, alpha=1, beta=2, evaporation_rate=0.5)
best_schedule, best_makespan = aco.run()

print("\nBest Schedule:", best_schedule)
print("Best Makespan:", best_makespan)

# Visualize the Results
plot_gantt_chart(best_schedule, processing_times)
