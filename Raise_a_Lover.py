import random

class lover:
    def __init__(self,name):
        self.name = "Akio"
        self.affection = 0
        self.level = 0
        self.health = 100
              
    def level_up(self):
        self.level += 1
        print(f"{self.name}'s affection leveled up to level {self.level}!")

    def gain_affection(self, affection):
        self.affection += affection        
        if self.affection >= 100:
            self.level_up()
            self.affection = 0
            
    def is_alive(self):
        return self.health > 0
        
            
class player:
         def __init__(self,name):
            name = input("Enter your name:")
            self.name = name
            
class game:
    def __init__(self):
        self.player = player("self.player.name")
        self.lover = lover("Akio")        
        
    def start_game(self):
         print (f"Welcome to Raise-A-Lover, {self.player.name}")
         while self.lover.is_alive():
               print(f"{self.lover.name}'s  affection :{self.lover.affection}")           
               action = input("What do you want to do? (talk/headpats/gift)")
               if action == "talk":
                 self.player_talk ()
               elif action == "headpats":
                 self.player_headpats ()
               elif action == "gift":
                 self.player_gift ()
               else:
                 print("Invalid action")
                 self.start_game() 
                        
    def player_talk (self):
             print (f"{self.player.name}: How are you today Akio?")
             responses = ["Good thank you!", "Just fine I guess", "Happy now that you're here~"]
             response = random. choice(responses)
             print (f"Akio: {response}")
             print (f"Akio's level: {self.lover.level}")
             affection = random.randint(5,10)
             self.lover.affection += affection 
            
    def player_headpats (self):
              print (f"{self.player.name}: My lovely Akio wants headpats~ ")
              responses = ["I- I do not! Stop that!", "Ehehehe~ More please!", "This is nice...thank you "]
              response = random. choice(responses)
              print (f"Akio: {response}")
              affection = random.randint(15, 30)
              self.lover.affection += affection 
 
    def player_gift (self):
            print (f"{self.player.name}: Tada! It's a gift, open it!")
            responses = ["Wow! I've been wanting this for a long time, thank you!", " That's so sweet of you thanks~", "This is amazing , you're the best!"]
            response = random. choice(responses)
            print (f"Akio: {response}")
            affection = random.randint(30,50)
            self.lover.affection += affection 
            
game = game()
game.start_game()