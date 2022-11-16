from random import *

MIN_SIDE = 4
def main():
    print("Dice roll Simulation")
    num_sides = int(input('How many sides should the die have: '))
    if num_sides < MIN_SIDE:
        num_sides = MIN_SIDE
    value = rollDice(num_sides)
    print("You rolled a dice", value)

# Simulate throwing two nsided dice
def rollDice(nSides):
    die1 = randint(1, nSides+1)
    die2 = randint(1, nSides+1)
    return die1 + die2

main()
