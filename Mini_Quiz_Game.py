name = input("name:")
print("Welcome to the game," + name)
print("Answer the questions and win a prize!")
answer = input("Are you ready?")
if answer == "yes":
    print ("Let's start!")
else:
    print("Yes you are now let's start")
    
questions = [
    ("Give a state of matter", ["Solid","solid", "Liquid","liquid", "Gas", "gas"]),
    ("What is the basic unit of life?", ["Cell", "cell"]),
    ("What color has the longest wavelength?", ["Red", "red"])
]

score = 0

for question, correct_answers in questions:
    print(question)
    user_answer = input("Answer: ")
    if user_answer in correct_answers:
        score += 1
        print("Correct!")
    else:
        print("Sorry, try again next time")
        
if score == 0:
 print("Sorry, you didn't win anything")
elif score == 3:
 print ("Congratulations! you won a trophy!")
else: 
 print("Congratulations, You won a rose!")