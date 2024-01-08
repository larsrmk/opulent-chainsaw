import random

def player_choice():
    print("1. rock\n2. paper\n3. scissors")
    return input("Choose 1/2/3: ")

    

def computer_choice():
    return str(random.randint(1, 3))



def result(player_choice, computer_choice):
    print("You selected {player_choice}.")
    print("The computer selected {computer_choice}.")

    if player_choice == computer_choice:
        return "Draw!"
    elif (player_choice == "1" and computer_choice == "3") or \
        (player_choice == "2" and computer_choice == "1") or \
        (player_choice == "3" and computer_choice == "2"):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == "__main__":
    print("Welcome to rock, paper, scissors.")

    while True:
        game = result(player_choice(), computer_choice())
        print(game)
    
        repeat=input("One more game (y/n)? ").lower()
        if repeat != "y":
            print("See ya!")
            break