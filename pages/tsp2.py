# After finding the minimum distance and shortest path, generate the plot
if st.button("Run Genetic Algorithm"):
    best_mixed_offspring = run_ga(cities_names, n_population, n_generations, crossover_per, mutation_per)
    
    # Calculate the minimum distance
    total_dist_all_individuals = []
    for i in range(0, n_population):
        total_dist_all_individuals.append(total_dist_individual(best_mixed_offspring[i]))
    index_minimum = np.argmin(total_dist_all_individuals)
    minimum_distance = min(total_dist_all_individuals)
    st.write("Minimum Distance : ", minimum_distance)

    # Retrieve the shortest path
    shortest_path = best_mixed_offspring[index_minimum]
    st.write("Shortest Path : ", shortest_path)

    # Plotting the shortest path
    x_shortest = []
    y_shortest = []
    for city in shortest_path:
        x_value, y_value = city_coords[city]
        x_shortest.append(x_value)
        y_shortest.append(y_value)

    # Close the path loop
    x_shortest.append(x_shortest[0])
    y_shortest.append(y_shortest[0])

    fig, ax = plt.subplots()
    ax.plot(x_shortest, y_shortest, '--go', label='Best Route', linewidth=2.5)
    plt.legend()

    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            ax.plot([x[i], x[j]], [y[i], y[j]], 'k-', alpha=0.09, linewidth=1)

    plt.title(label="TSP Best Route Using GA", fontsize=25, color="k")

    # Additional information on the plot
    str_params = f'\n{n_generations} Generations\n{n_population} Population Size\n{crossover_per} Crossover\n{mutation_per} Mutation'
    plt.suptitle(f"Total Distance Travelled: {round(minimum_distance, 3)}" + str_params, fontsize=18, y=1.047)

    for i, txt in enumerate(shortest_path):
        ax.annotate(str(i+1) + "- " + txt, (x_shortest[i], y_shortest[i]), fontsize=20)

    fig.set_size_inches(16, 12)
    st.pyplot(fig)
