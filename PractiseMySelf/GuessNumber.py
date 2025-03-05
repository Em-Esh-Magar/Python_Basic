import random

value = random.choice(range(0,101))

num_of_try = 0
user_value = 1

print("Enter a number from 0-100")

while(user_value != value):
    user_value = int(input("Enter a number : "))
    
    if user_value<0 or user_value>100:
        print("Invalid value. \n Enter a number between 0-100")
    
    else:
        if(user_value == value):
            num_of_try+=1
            print(f"Congratulation you have guessed successfully in {num_of_try} tries")
            break;
    
        elif user_value > value:
            print("You have entered the greater value than the real value")
            num_of_try+=1
        
        elif user_value < value:
            print("You have entered the smaller value than the real value")
            num_of_try+=1
        
        else:
            continue
        