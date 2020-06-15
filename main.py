import bio_sim as bs
import os, sys

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

NUM_SIMULATIONS = 10
NUM_DAYS = 30


print("Biological simulation with SimPy.")

results = []
# In this way the print statements in bs.main() are suppressed
with HiddenPrints():
    for i in range(NUM_SIMULATIONS):
        results.append(np.array(bs.main()))
results = np.array(results)

mean_blobs = np.mean(results, axis=0)
std_blobs = np.sqrt(np.var(results, axis = 0))

savetxt('Results.csv', results, fmt='%10.5f')

print("Mean Blobs per day:", mean_blobs)
print("Var Blobs per day:", std_blobs)

plt.hlines(70, xmin=0, xmax=30, linestyle='dashed', linewidth=1, label='Food Level')
plt.errorbar(np.arange(30), mean_blobs, yerr=std_blobs, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=4, ecolor='red', label='Blobs')
plt.legend()
plt.show()
