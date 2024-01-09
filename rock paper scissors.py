import random

def player_choice():
    print("1. rock\n2. paper\n3. scissors")
    return input("Choose 1/2/3: ")

def computer_choice():
    return str(random.randint(1, 3))

def result(pc, cc):
    print(f"You selected {pc}.")
    print(f"The computer selected {cc}.")

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
        pc = player_choice() 
        cc = computer_choice()

        game = result(pc, cc)
        print(game)
    
        repeat=input("One more game (y/n)? ").lower()
        if repeat != "y":
            print("See ya!")
            break