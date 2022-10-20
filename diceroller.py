import random

def rolldice(min, max):
    while True:
        print("rolling the dice...")
        print(f"your number is: {random.randint(min,max)}")
        choice = input("do you wanna roll again? ")
        if choice.lower() != "yes":
            break

rolldice(1,6)
