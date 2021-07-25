if __name__ == "__main__":
    secret_nb = '42'
    u_input = 'a'
    nb_attempt = 1
    print("This is an interactive guessing game!");
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")

    while u_input != secret_nb and u_input != 'exit':
        print("What's your guess between 1 and 99?\n>>", end='')
        u_input = input()
        try:
            u_nb = int(u_input)
            if u_nb > int(secret_nb):
                print("Too high!")
            elif u_nb < int(secret_nb):
                print("Too low!")
            else:
                break
        except BaseException:
            if u_input != 'exit':
                print("That's not a number.")
        nb_attempt += 1
    if u_input.isdigit() and u_input == secret_nb:
        if secret_nb == "42":
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if nb_attempt == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in {} attempts!".format(nb_attempt))
    else:
        print("Goodbye!")
