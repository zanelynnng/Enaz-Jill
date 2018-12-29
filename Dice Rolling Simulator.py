import random

print("This is a dice guessing game. You have 3 tries")

guesstaken = 0
maxguess = 3
dicenumber = random.randint(1,6)
print(dicenumber)

while guesstaken < maxguess:
    try:
        mynumber = raw_input("Try a number: ")
        mynumber = int(mynumber)

        if mynumber < 1 or mynumber > 6:
            print("a Dice has number 1,2,3,4,5 and 6 only. Try again")
        else:
            guesstaken = guesstaken + 1

            if mynumber > dicenumber:
                print("guess is too high")
                guessleft = maxguess - guesstaken
                guessleft = str(guessleft)
                print("You have " + guessleft + " tries left")

            elif mynumber < dicenumber:
                print ("guess is too low")
                guessleft = maxguess - guesstaken
                guessleft = str(guessleft)
                print("You have " + guessleft + " tries left")

            elif mynumber == dicenumber:
                guesstaken = str(guesstaken)
                print("you got it in " + guesstaken + " tries")
                break
    except ValueError:
        print("That is not a number")

if guesstaken == maxguess:
    print("you have guessed 3 times and failed")





