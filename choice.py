import time
import random

hej = []
numberofchoices = int(input("How many inputs do you want?: "))

for i in range(numberofchoices):
    hej.append(input("Input Option: "))

choice = random.choice(hej)

print(f"The selected choice is: {choice}")