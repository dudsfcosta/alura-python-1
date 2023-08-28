print("Welcome to the Akinator!")

secret_number = 42
guess = 0
curr_round = 0
total_round = 10

for curr_round in range(0,10):
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
            print("You're right!")
            break

        else:
            if guess > secret_number:
                print("You're wrong! Your guess is bigger than the secret number.")
            else:
                print("You're wrong! Your guess is lower than the secret number.")

print("End of game.")
