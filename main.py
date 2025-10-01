import random

import genetic_algo as ga
import tetris_base as game
import play_ai as ai
import copy
import chromosome as chromosome
import numpy as np
np.random.seed(25)
import matplotlib.pyplot as plt


def get_best_two(generation):
    best_chromo = generation[0]
    for g in generation:
        if g.fitness_score > best_chromo.fitness_score:
            best_chromo = g
    second_best_chromo = generation[1]
    for g in generation:
        if g.fitness_score > second_best_chromo.fitness_score and g != best_chromo:
            second_best_chromo = g
    return [best_chromo, second_best_chromo]

def plot(best_two_over_generations):
    # Example data (replace with your actual data)
    chromosome1_scores = []  # Scores of best chromosome 1
    chromosome2_scores = []  # Scores of best chromosome 2
    generations = list(range(1, 21))  # Generation numbers
    for g in best_two_over_generations:
        chromosome1_scores.append(g[0])
        chromosome1_scores.append(g[1])

    # Create the plot
    plt.plot(generations, chromosome1_scores, label='Best Chromosome 1')
    plt.plot(generations, chromosome2_scores, label='Best Chromosome 2')

    # Add labels and title
    plt.xlabel('Generation')
    plt.ylabel('Score')
    plt.title('Progress of Best Two Chromosomes\' Scores')
    plt.legend()

    # Show the plot
    plt.show()


def train():
    population_num = 20
    mut_rate = 0.2
    evaluation_num = 19
    init_pop = ga.generate_pop(population_num)
    generations = []
    pp = 1
    pop = copy.deepcopy(init_pop)
    best_two_over_generations = []
    for i in range(evaluation_num):
        best_two_over_generations.append(get_best_two(pop))
        for chrom in pop:
            game_state = ai.play_game(chrom, 600, 20000)
            chrom.fitness_score = ga.calculate_fitness_score(game_state[1], game_state[0], game_state[2]) + game_state[2] * 500
            chrom.scores.append(chrom.fitness_score)
            print(pp)
            pp += 1
        selected_parents = ga.parents_selection(pop, 7)
        offspring = ga.crossover(selected_parents)
        mutated_children = ga.mutation(offspring, mut_rate)
        generations = mutated_children
        pop = generations
        print("generation:", i+1)
        for g in generations:
            game_state = ai.play_game(g, 600, 20000)
            g.score = game_state[1]
            g.fitness_score = ga.calculate_fitness_score(game_state[1], game_state[0], game_state[2])
            g.scores.append(g.fitness_score)
        best_chromo = generations[0]
    for g in generations:
        if g.fitness_score > best_chromo.fitness_score:
            best_chromo = g
    second_best_chromo = generations[1]
    for g in generations:
        if g.fitness_score > second_best_chromo.fitness_score and g != best_chromo:
            second_best_chromo = g
            # optimal_weights
    best_two_over_generations(pop)
    plot(best_two_over_generations)
    print(best_chromo.weights)
    print(best_chromo.fitness_score)
    print(second_best_chromo.weights)
    print(second_best_chromo.fitness_score)
    # Open a file in append mode
    with open('output.txt', 'a') as file:
        # Append content to the file
        for w in best_chromo.weights:
            file.write(str(w) + '\n')
        file.write(str(best_chromo.fitness_score)+'\n')
        for w in second_best_chromo.weights:
            file.write(str(w) + '\n')
        file.write(str(best_chromo.fitness_score)+'\n')

    ai.play_game(best_chromo, 600, 10000)


def test():
    weights = []
    with open('output.txt', 'r') as file:
        # Read each line of the file
        line_number = 0
        for line in file:
            # Convert the line to a float and append it to the list
            weights.append(float(line.strip()))

            # Increment the line number
            line_number += 1

            # Check if we have read 9 lines
            if line_number >= 9:
                break
    best_chromosome = chromosome.Chromosome(weights)
    ai.play_game(best_chromosome, 600, 10000)


def main():
    choice = 1
    choice = int(input("1-train\n2-test\n"))
    if choice == 1:
        train()
    elif choice == 2:
            # optimal = [-13.81094188838252, -10.303344683076283, -2.8335800910005897, 1.0994559042575887, -0.30171731559318005, -13.209916777215414, 7.992216011063988, -6.791122871910307, 7.240959342179323]
            # optimal = [-6.209064291089264, -11.69954550398876, -5.880393706512153, 5.39250279348947, -8.86541219139536, -7.77828212879005, 9.481580815982909, 5.6212923028684685, 9.350856792670243]
            # optimal = [-5.137631351988473, -14.632849827282865, -11.604318804976899, 6.608115510228124, -13.129803932028661, -0.09457603593610742, 12.020865679669217, -5.35787917313815, 14.765451714516086]
            # optimal = [-5.137631351988473, -14.632849827282865, -11.604318804976899, 6.608115510228124, -13.129803932028661, -0.09457603593610742, 12.020865679669217, -5.35787917313815, 14.765451714516086]
            # optimal = [-10.25117860280572, -6.244069325401414, -10.264571943106347, 9.404262706188103, -3.9005873006862295, -5.335088297813636, 6.285935195146056, -14.46793779645933, 7.698011458214371]
            # optimal = [8.635256268873182, -13.003193533746206, -4.87069495928756, 11.810933270320405, -2.8004289310418162, 7.821448603389715, 8.297262556673676, -6.401191201032724, 3.210030761736963]
            # optimal = [-2.065990240763254, -14.444581887527047, -7.5761975671280455, 9.008780942928126, -9.209605243723544, 2.8183824687158676, -3.266240484756162, 7.03297701806359, 3.529220455084065]
            # ai.play_game(chromosome.Chromosome(optimal), 600, 10000)
            # # ai.play_game(best_chromo, 600, 1000)
        # with open('output.txt', 'r') as file:
        #     optimal_weights = file.readline()
        optimal_weights = [0.2530608024214196, -14.438352051269522, -11.063916309362135, -3.17490590721966, -1.1900825280325726, -0.43086274558272386, 11.376988496280067, 6.4402287985849895, 6.34762111076482]
        ai.play_game(chromosome.Chromosome(optimal_weights), 600, 10000)


if __name__ == '__main__':
    main()

"""
[0.2530608024214196, -14.438352051269522, -11.063916309362135, -3.17490590721966, -1.1900825280325726, -0.43086274558272386, 11.376988496280067, 6.4402287985849895, 6.34762111076482]
56.865921787709496
[0.2530608024214196, -14.438352051269522, -11.063916309362135, -3.17490590721966, -1.1900825280325726, -0.43086274558272386, 11.376988496280067, 6.4402287985849895, 6.34762111076482]
49.87780548628429
"""
