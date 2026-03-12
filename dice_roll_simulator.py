#Dice Rolling Game
import random
import time

counter = 0

while True:
    choice = input("\nRoll the dice?  (y/n): ").lower()    
    if choice == "y":
        num = int(input("Number of Dice: "))
        print("\nRolling....\n")
        time.sleep(0.5)
        
        for i in range(1, num + 1):
            a = random.randint(1, 6)
            counter += 1
            print(f"Dice {i}: {a}")
        print(f"Number of Dice rolled: {counter}")    
       
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
        

        
    