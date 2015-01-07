#!/usr/bin/env python3

#Philip Hansen 2015

import random

def gen_math():
    signs = ["+", "-"]

    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    sign = signs[random.randint(0, 1)]

    question = (str(number_1) + sign + str(number_2))
    answer = eval(question)

    return question, answer

def quiz():
    global points

    question, answer = gen_math()

    print("Your question is: " + question)
    given_answer = int(input("Answer: "))

    if given_answer == answer:
        points += 1
        print("Correct!")
    else:
        print("Wrong, the correct answer was " + str(answer))

def main():
    global points

    points = 0
    rounds = 10

    for i in range(rounds):
        quiz()
    #Once the for loop is done
    else:
        print("You completed the game with " + str(points) + "/" + str(rounds) + " points.")

if __name__ == "__main__":
    main()
