import random

print("welcome to a wonderful game.""\n" "A number guess game")

print("rules","\n","you have only 7 chances to guess a number")

print("lets  begin")

low=int(input("enter a lower nuber:"))
high=int(input("enter a higest number:"))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low,high)
nc=7
gc=0

while gc < nc:
    gc += 1     
    guess=int(input("enter a number you guess: "))

    if num == guess:
        print("well done ", "\n" ,"your guess is:", guess,"is correct")
        break

    elif gc >= nc and  num != guess:
        print("your guess of number", guess, "is in correct","\n", "better luck next time" )

    elif guess > num:
        print("your guess is too high")
    elif guess < num:
        print("your guess is too low")
