import random

choices = ["R", "P", "S"]
print("Welcome to the game of rock, paper, scissor!!!")
print("Instructions: [P] = Paper , [R] = Rock,  [S] = Scissors , [Q] = Quit")


def get_input(input):
    if input == "R":
        return "Rock"
    elif input == "P":
        return "Paper"
    elif input == "S":
        return "Scissors"
    elif input == "Q":
        return "Quit"
    else:
        return "Incorrect input"


counter = 1
while True:
    print("Game " + str(counter) + ":")
    print("Enter your choice : ")
    user_input = input()
    user_choice = get_input(user_input)

    random_index = random.randint(0, 2)
    computer_input = choices[random_index]
    computer_choice = get_input(computer_input)


    def print_choices(user_choice, computer_choice):
        print("You chose " + str(user_choice) + " and the computer chose " + str(computer_choice) + ".")


    if user_input == "Q":
        print("Well played, come again soon!!!")
        break;
    elif user_input == "R" and computer_input == "S":
        print_choices(user_choice, computer_choice)
        print("You win, Rock beats Scissors")
    elif user_input == "P" and computer_input == "R":
        print_choices(user_choice, computer_choice)
        print("You win, Paper beats Rock")
    elif user_input == "S" and computer_input == "P":
        print_choices(user_choice, computer_choice)
        print("You win, Scissors beats Paper")
    elif user_input == "R" and computer_input == "P":
        print_choices(user_choice, computer_choice)
        print("Computer wins, Paper beats Rock")
    elif user_input == "P" and computer_input == "S":
        print_choices(user_choice, computer_choice)
        print("Computer wins, Scissors beats Paper")
    elif user_input == "S" and computer_input == "R":
        print_choices(user_choice, computer_choice)
        print("Computer wins, Rock beats Scissors")
    elif user_input == computer_input:
        print("You chose " + str(user_choice) + " and the computer also chose " + str(computer_choice) + ".")
        print("It's a tie")
    else:
        print("Please Enter the correct input")
    counter = counter + 1
    print("\n")
