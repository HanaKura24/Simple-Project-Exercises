#Score Tracker (might crash when user input alphabet )

score = 0

def add_score(score, points):
    new_score = score + points
    
    if new_score < 0:
        new_score = 0
        
    return new_score
        

score = add_score(score, -20)
print(score)

score = add_score(score, 19)
print(score)

score = add_score(score, 8)
print(score)

#Multiple Round Score Tracker

score = 0
points = ""
def update_score(score, points):
    new_score = score + points
    
    if new_score < 0:
        new_score = 0
        
    return new_score
    
while points != "q":
    points = input("Enter points (or q to quit): ")
    
    if points == "q":
        print(f"Final score: {score}")
    
    else:
        points = int(points)
        score = update_score(score, points)
        print(f"Score: {score}")


   
