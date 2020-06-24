#! usr/bin/env python3

"""

Biological system simulation using Simpy.

Stefano Mangini, UniPv, 2020.

"""

import bio_sim as bs
import averages as mn
import os, sys
from tqdm import tqdm
from scipy import stats

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


print("Main_Stat.py - Biological simulation with SimPy.")

### Run the main.py file multiple times changing the food_rate_production parameters, and saves the ending food level and living blob Number
### for further plotting and analysis

results = []
foods = []
food_rates_list = [10*i for i in range(1,20)]
# In this way the print statements in bs.main() are suppressed
with HiddenPrints():
    for foodrate in tqdm(food_rates_list):
        # results.append(np.array(bs.main(start_blob = NUM_BLOB, start_food = INITIAL_FOOD, food_rate = FODD_RATE_PRODUCTION)))
        _res = mn.main(food_rate_production = foodrate, plotting = False)
        results.append(np.array(_res[0]))
        foods.append(np.array(_res[1]))

results = np.array(results)
foods = np.array(foods)

# Linear fit of the data using SciPy
slope, intercept, r_value, p_value, std_err = stats.linregress(foods, results)
def predict_y_for(x):
    return slope * x + intercept

print("")
print("Slope:", slope)
print("Intercept:", intercept)


# Plot of the data
plt.scatter(foods, results, color='green', marker='o')
plt.plot(foods, predict_y_for(foods), c='orange', linestyle="dashed")
plt.ylabel('Number of living blobs at equilibrium')
plt.xlabel('Food level at equilibrium')
plt.title(f'Slope ~ {round(slope,3)}, Intercept ~ {round(intercept,3)}')
plt.grid(linestyle='--', linewidth=1)
plt.show()
