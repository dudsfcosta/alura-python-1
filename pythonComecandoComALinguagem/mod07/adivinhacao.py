import random

print("Welcome to the Akinator!")

guess = 0
curr_round = 0
secret_number = random.randrange(1,101)
flag = False
points = 1000
# randrange gets a number between a starting point (inclusive) and
# an endpoint (exclusive) following certain steps (optional)

print("secret number : ", secret_number)

print("Please select difficulty:\nEasy(1)\nNormal(2)\nHard(3)")
level = int(input())

if level == 1:
    total_round = 20
elif level == 2:
    total_round = 10
else:
    total_round = 5

while curr_round < total_round:
    print("You are in the round of number {}. There are {} rounds remaining.".format(curr_round+1, total_round-curr_round-1))
    guess = int(input("Type a number between 0 and 100: "))
    print("You typed: ", guess)

    # variables for better legibility
    hit = guess == secret_number    # compares guess with secret number. If equal, its false

    if guess < 0 or guess > 100:
        print("You must type a number between 0 and 100!")
        # curr_round -= 1
    else:
        if hit:
            print("You're right! Your got ", points, " points.")
            break

        else:
            if guess > secret_number:
                print("You're wrong! Your guess is bigger than the secret number.")
            else:
                print("You're wrong! Your guess is lower than the secret number.")
            lost_points = abs(secret_number - guess)
            points -= lost_points
    curr_round += 1

print("End of game.")
