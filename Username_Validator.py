#User Name Validator

 #Length is between 4 and 12 characters
# Contains only letters and numbers
# Must start with a letter
# No spaces allowed

running = True
    
def validate_username(username, running):
    error = 0
    
    if len(username) < 4 or len(username) > 12:
        print("❌ Username must contain 4-12 characters only, try again")
        error += 1
        
    if not username.isalnum():
        print("❌ Username must not contain special characters or spaces, try again")
        error += 1
        
    if not username[0].isalpha():
        print("❌ Username must start with a letter, try again")
        error += 1
        
    if error == 0:
        print("✅ Username Validated")
        running = False
        
    return running
    
        
while running:
    username = input("\nUsername: ")
    running = validate_username(username, running)
    