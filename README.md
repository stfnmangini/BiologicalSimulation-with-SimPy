# Simulation of a Biological system using Simpy

This Python project uses SimPy, a discrete time simulation framework, to simulate the evolution of a population of living creatures in an environment with limited food supply.  
The main idea behind the simulation is from Primer's youtube video on [Natural Selection](https://www.youtube.com/watch?v=0ZGbIKd0XrM), but simpler and without any video rendering.

SimPy may not be the best tool for implementing this kind of biological simulations, but since I had to make a Python project with it, I decided to give it a try with the natural selection simulation.

The file is well documented, so it should not be hard to understand.

### Useful information in the simulations
* A *Forest* is the natural environment where the living creatures, called *Blobs*, live. The simulation is divided into days, and each day has a _daylight_ and _nighttime_ period. During _daylight_ the Blobs goes searching for food, while during _nighttime_ they go to sleep and wait for the next day to begin.

* The *Blob* is the living creature populating the *Forest*. Each Blob goes searching for food during daylight, and rest during nighttime.
The Blob has to eat a minimum amount of food each day to survive, otherwise it dies. 
