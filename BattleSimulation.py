'''
From FiveThirtyEight's Riddler classic: A Long Night Simulation

Riddler Link: https://fivethirtyeight.com/features/how-many-soldiers-do-you-need-to-beat-the-night-king/

Each army lines up single file, facing the other army.
One soldier steps forward from each line and the pair duels — 
half the time the living soldier wins, half the time the dead soldier wins. 
If the living soldier wins, he goes to the back of his army’s line, 
and the dead soldier is out
(the living army uses dragonglass weapons, so the dead soldier is dead forever this time).
If the dead soldier wins, he goes to the back of their army’s line, but this time the (formerly) living soldier joins him there.
(Reanimation is instantaneous for this Night King.)
The battle continues until one army is entirely eliminated.
'''
from random import randrange

def battle_simulation(living_army_size, dead_army_size):
    living_army = [1]*living_army_size
    dead_army = [1]*dead_army_size
    
    while living_army and dead_army:
        outcome = randrange(0, 2)
        if outcome == 1:
            dead_army.pop()
        else:
            living_army.pop()
            dead_army.append(1)
    
    #return 1 if living win, 0 if dead win
    if living_army:
        return 1
    else:
        return 0
