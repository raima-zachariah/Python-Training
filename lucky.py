import random

def lucky_no():
    return random.randint(1,25)

def validate(user_no, lucky):
    flag = False
    close_guess = False
    if user_no == lucky:
        print("You guessed it right")
        flag = True
    elif user_no in range(lucky-2, lucky+3):
        print("You are close")
        close_guess = True
    elif user_no > lucky:
        print("too high")
    else:
        print("too low")

    return  flag, close_guess
            
def check_no(chance, lucky):
    while chance > 0:
        user_no = int(input("Make your guess: "))
        flag, close_guess = validate(user_no, lucky)   
        chance -= 1
    return flag, close_guess
        
if __name__ == "__main__":
    lucky = lucky_no()
    print(lucky)
    flag,close_guess = check_no(4,lucky)
    if close_guess == True:
        flag, close_guess = check_no(1,lucky)
        
    if not flag:
        print("Oops!! tries over")
        print("the lucky number is:", lucky)
            
