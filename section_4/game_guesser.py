from typing import AnyStr


print("Guess a number between 1 and 100 : ")
user_guess = int(input())

answer = 5

if user_guess > answer:
    print("Guess a lower number")
elif user_guess < answer:
    print("Guess a higher number")
else:
    print("You Won")


