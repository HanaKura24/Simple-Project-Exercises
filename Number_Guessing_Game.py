#Guessing Game
import random

print("\n\t\tGuess the Number: Guessing Game")

class Game:
    def __init__ (self):
        name = input("Name: ")
        self.name = name
        
    def start_game(self):
        lower_boundary = int(input("\nLower Boundary: "))
        upper_boundary = int(input("Upper Boundary: "))
        
        num= random.randint(lower_boundary, upper_boundary)
        attempts = 0
        guess = 0
        
        while guess != num:
            attempts+= 1
            print(f"\nGuess {attempts}: ")
            guess = int(input(">> "))
            
            if guess == num:
                print("\nCongratulations, you won!")
                print(f"It took {self.name} {attempts} attempt/s to guess the number right")
                game.restart_game()
            elif guess > num:
               print("Wrong, guess lower")
            elif guess < num:
               print("Wrong, guess higher")
               
    def restart_game(self):
           choice =  input("\nDo you want to continue playing?\n>> ")

           if choice == "yes":
            game.start_game()
           elif choice == "no":
             print(f"\nThank you for playing {self.name}")
           else:
               print("Please only type yes or no")
               game.restart_game()
               
game = Game()
game.start_game()