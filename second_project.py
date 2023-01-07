import random



top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("please enter an number next time.")
    quit()

guesses = 0

random_number = random.randint(0, top_of_range)


while True:
    guesses =guesses+1
    user_guess = input("Make an guess : ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please enter an number next time.")
        continue


    if user_guess == random_number:
        print("Hurray,You got it!!!")
        break
    elif user_guess < random_number:
        print("You are below the number.")
    else:
        print("you are above the number.")

        

print("you got in",guesses,"guesses")





