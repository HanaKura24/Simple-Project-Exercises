print("Odd or Even?")

prompt = ""
while prompt != "quit":
 prompt = input("\nEnter a number and I'll tell if its Odd or Even\n>")
 if prompt == "quit":
   print("\nThank you for playing")
 else:
   num = int(prompt)
   if num % 2 == 0:
     print(f"The number {num} is EVEN")
   else:
     print(f"The number {num} is ODD")
    
