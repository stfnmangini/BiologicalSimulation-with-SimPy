#! usr/bin/env python3

"""

Biological system simulation using Simpy.

Stefano Mangini, UniPv, 2020.

"""

import bio_sim as bs
import os, sys
from tqdm import tqdm

import numpy as np
from numpy import savetxt

import matplotlib.pyplot as plt

class HiddenPrints:
    """
    Useful Context manager to suppress the print statements in called functions.
    To be used with the 'with' syntax (see code below).
    """
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def main(food_rate_production = 100, plotting = True):

    NUM_SIMULATIONS = 100 # Number of simulations for botaining a statistics
    NUM_DAYS = 50 # Number of days in a single simulation
    NUM_BLOB = 100 # Number of Blobs (the living creature poppulating the Environment).
    INITIAL_FOOD = 100 # starting food availability in the environment
    # FOOD_RATE_PRODUCTION = 150 # each day 100 more food is produced by the environment
    FOOD_RATE_PRODUCTION = food_rate_production # each day 100 more food is produced by the environment


    print("Biological simulation with SimPy.")

    # Executes bio_sim multiple time with the same parameters in order to evaluate avarages quantities thus reaching more reliable and useful information.

    results = []
    foods = []
    # In this way the print statements in bs.main() are suppressed
    with HiddenPrints():
        for i in tqdm(range(NUM_SIMULATIONS)):
            # results.append(np.array(bs.main(start_blob = NUM_BLOB, start_food = INITIAL_FOOD, food_rate = FODD_RATE_PRODUCTION)))
            _res = bs.main(start_blob = NUM_BLOB, start_food = INITIAL_FOOD, food_rate = FOOD_RATE_PRODUCTION, num_days = NUM_DAYS)
            results.append(np.array(_res[0]))
            foods.append(np.array(_res[1]))

    results = np.array(results)
    foods = np.array(foods)

    # Some processing of the data with Numpy builtin functions 'mean' ans 'std'
    mean_blobs = np.mean(results, axis=0)
    std_blobs = np.sqrt(np.var(results, axis = 0))

    mean_foods = np.mean(foods, axis=0)
    std_foods = np.sqrt(np.var(foods, axis=0))

    savetxt('./Results.csv', results, fmt='%10.5f')

    print("Mean Blobs per day:", mean_blobs)
    print("Var Blobs per day:", std_blobs)

    # PLOT OF RESULTS
    if plotting:
        # plt.hlines(FODD_RATE_PRODUCTION, xmin=0, xmax=30, linestyle='dashed', linewidth=1, label='Food rate production')
        # plt.hlines(INITIAL_FOOD, xmin=0, xmax=30, linestyle='dashed', linewidth=1, label='Initial Food Level')
        plt.plot([],[], linewidth = 0, label=f'Food rate production = {FOOD_RATE_PRODUCTION}')
        plt.errorbar(np.arange(NUM_DAYS), mean_foods, yerr=std_foods, color = 'orange', marker = 'X', linestyle='dashed', linewidth=2, markersize=4, ecolor='blue', label='Food level')
        plt.errorbar(np.arange(NUM_DAYS), mean_blobs, yerr=std_blobs, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=4, ecolor='red', label='Blobs')
        plt.xlabel('Days')
        plt.legend()
        plt.show()

    return mean_blobs[-1], mean_foods[-1]

if __name__ == '__main__':
    do_plot = True
    main(plotting = do_plot)
