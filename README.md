# Simulation of a Biological system using SimPy

This Python project uses SimPy, a discrete time simulation framework, to simulate the evolution of a population of living creatures in an environment with limited food supply.  
The main idea behind the simulation is from Primer's youtube video on [Natural Selection](https://www.youtube.com/watch?v=0ZGbIKd0XrM), but simpler and without any video rendering.

SimPy may not be the best tool for implementing this kind of biological simulations, but since I had to make a Python project with it, I decided to give it a try with the natural selection simulation. Probably the bes solution for this kind of simulation would be using OOP (Object Oriented Programming), and constantly looping and updating the state of the living creatures, until the end of the simulation.

The fils are well documented, so it should not be hard to understand.

### *bio_sim.py*: Useful information for the simulation
* A *Forest* is the natural environment where the living creatures, called *Blobs*, live. The simulation is divided into days, and each day has a _daylight_ and _nighttime_ period. During _daylight_ the Blobs goes searching for food, while during _nighttime_ they go to sleep and wait for the next day to begin.

* The *Blob* is the living creature populating the *Forest*. Each Blob goes searching for food during daylight, and rest during nighttime.
The Blob has to eat a minimum amount of food each day to survive, otherwise it dies. The process of finding food takes a random time, and after the Blob found and ate the food, it rests for a while before going hunting again. If It eats more food than required to survive, it reproduces, thus creating another Blob in the simulation.

### *main.py*  
This file executes the simulaton in *bio_sim.py* multiple times in order to achieve a sufficient statistics to plot relevant information and results of the simulation.


### *main_stat.py*
This file extrapolates relevant information when an equilibrium between available food and blobs is reached and fits the data.

### *Presentation*
The folder contains a presentation, further explaining the code, its motivations, difficulties encountered and final thoughts.

### Required packages (installation with Conda)
- Simpy: [Simulation Package in Python](https://simpy.readthedocs.io/en/latest/)
```
conda install -c mutirri simpy
```
- Tqdm: Useful [Prograss Bar](https://tqdm.github.io/) for Python
```
conda install -c conda-forge tqdm
```
- Scipy: for linear fitting of data
```
conda conda install -c anaconda scipy
```
- Numpy and Matplotlib
