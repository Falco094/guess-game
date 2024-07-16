import random 

def guessing_game():
    number_guess = random.randint(1,100)
    attemps = 0
    
    while True:
        guess = int(input("enter a number"))
        attemps += 1
        
        if guess > number_guess:
            print("High")
            
        elif guess < number_guess:
            print("low")
            
        else:
            print("Correct in {attemps} attemps")
            break
        
        if attemps > 5 :
            print("you reached your limit")
            break
        
        
guessing_game()

