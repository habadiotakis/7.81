import random
import math
import numpy as np
import matplotlib.pyplot as plt

### Line Generation Code

# n = 10
n = 500
s = 0.02

def identical_pop(population):
    individual_one = population[0]
    for i in population[1:]:
        if i != individual_one:
            return False
    return True

def moran_one_step(n,s):
    advantage = np.random.exponential(s)
    fitness = [1 for i in range(n-1)]
    fitness.append(1+advantage)
    probabilities = [i/np.sum(fitness) for i in fitness]

    all_same = False
    while not all_same:
        birth_choice = np.random.choice(range(n),p=probabilities)
        death_choice = np.random.choice(range(n))
        fitness.append(fitness[birth_choice])
        fitness.pop(death_choice)

        probabilities = [i/np.sum(fitness) for i in fitness]
        all_same = identical_pop(fitness)

    if fitness[0] == 1:
        return (advantage, 0)
    return (advantage,1)

x = []
y = []
total = []
for i in range(20):
    total.append(moran_one_step(n,s))
sorted_s = sorted(total, key=lambda run:run[0])
for entry in sorted_s:
    i,j = entry
    x.append(i)
    y.append(j)
y_str = ["No" if i==0 else "Yes" for i in y]

# histogram           
plt.hist(y_str)
plt.title("Distribution of Mutation Takeover; N = %s" % n)
plt.ylabel("Counts of Takeover")
plt.xlabel("Did it takeover?")
plt.show()

# cdf plot
plt.plot(x,np.cumsum(y)/np.sum(y))
plt.title("Cumulative Distribution of Mutation Takeover; N = %s" % n)
plt.ylabel("Probability of Takeover")
plt.xlabel("Advantage, s")
plt.show()