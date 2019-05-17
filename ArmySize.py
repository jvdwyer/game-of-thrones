from BattleSimulation import battle_simulation
from random import randrange
import matplotlib.pyplot as plt
import numpy as np

def random_army_size_simulation():
    living_army_size = []
    dead_army_size = []
    result = []
    conducted_simulations = 0

    while conducted_simulations < 10000:
        living = randrange(0,10000)
        dead = randrange(0, 300)
        outcome = battle_simulation(living, dead)
        living_army_size.append(living)
        dead_army_size.append(dead)
        result.append(outcome)
        conducted_simulations += 1
    
    living_army_size = [size/np.mean(living_army_size) for size in living_army_size]
    dead_army_size = [size/np.mean(dead_army_size) for size in dead_army_size]

    cs = []
    for o in result:
        if o == 1:
            cs.append('g')
        else:
            cs.append('r')

    plt.xlabel('Army of the Living Size')
    plt.ylabel('Army of the Dead Size')   
    plt.title('Long Night Simulation') 
    plt.scatter(living_army_size, dead_army_size, color = cs)
    plt.show()

random_army_size_simulation()