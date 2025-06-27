# dice_game.py
import random

name = input("What is your name?\n> ")
print(f"Hello, {name}!")

print("Rolling dice...")
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

print("Die 1:", die1)
print("Die 2:", die2)
print("Total value:", total)

if total > 7:
    print(f"{name} won!")
else:
    print(f"{name} lost!")
