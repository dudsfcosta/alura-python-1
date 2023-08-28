print("Welcome to the Akinator!")

secret_number = 42
guess = 0
curr_round = 0
total_round = 5

while (guess != secret_number) and (curr_round < total_round):
    print("You are in the round of number {}. There are {} rounds remaining.".format(curr_round, total_round-curr_round))
    guess = int(input("Type your number: "))
    print("You typed: ", guess)

    # variables for better legibility
    hit = guess == secret_number    # compares guess with secret number. If equal, its false
    bigger = guess > secret_number  # If bigger comes true

    if hit:
        print("You're right!")

    else:
        if bigger:
            print("You're wrong! Your guess is bigger than the secret number.")
        else:
            print("You're wrong! Your guess is lower than the secret number.")
    curr_round += 1

print("End of game.")
