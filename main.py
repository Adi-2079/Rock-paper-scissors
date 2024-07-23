from random import randint

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]
player = False
player_score = 0
high_scores = {}

def login():
    # Get the username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password are valid
    with open("users.txt", "r") as f:
        for line in f:
            line = line.strip()  # Remove leading/trailing whitespaces
            if not line:
                continue  # Skip empty lines

            try:
                user, passw = line.split()
                if username == user and password == passw:
                    print("Login successful!")
                    return username
            except ValueError:
                print("Invalid user data format in the file.")
                return None

    # Display an error message
    print("Invalid username or password")
    return None


def register():
    # Get the username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username already exists
    with open("users.txt", "r") as f:
        for line in f:
            line = line.strip()  # Remove leading/trailing whitespaces
            if not line:
                continue  # Skip empty lines

            try:
                user, passw = line.split()
                if username == user:
                    print("Username already taken")
                    return None
            except ValueError:
                print("Invalid user data format in the file.")
                return None

    # Write the username and password to the text file
    with open("users.txt", "a") as f:
        f.write(f"{username} {password}\n")

    print("Registration successful!")
    return username


def load_high_scores():
    try:
        with open("high_scores.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                user, score = line.split()
                high_scores[user] = int(score)
    except FileNotFoundError:
        pass


def save_high_scores():
    with open("high_scores.txt", "w") as f:
        for user, score in high_scores.items():
            f.write(f"{user} {score}\n")


def main():
    load_high_scores()
    
    while True:
        print("Welcome to the login system!")
        print("Choose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            username = login()
            if username:
                # Perform logged-in operations
                print("Logged in. Access granted.")
                break  # Exit the loop after successful login
        elif choice == "2":
            username = register()
            if username:
                # Perform post-registration operations
                print("Registration complete. You can now login.")
        elif choice == "3":
            break  # Exit the loop if the user chooses to quit
        else:
            print("Invalid choice. Please try again.")

    return username


# Call the main function to start the login system
username = main()

if username:
    while player == False:
        print("Let's play Rock, Paper, Scissors")
        player = input("Rock, Paper, Scissors: ").capitalize()
        
        if player == computer:
            print("It's a tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lost! Computer picked Paper.")
            elif computer == "Scissors":
                print("You won! Computer picked Scissors.")
                player_score += 1
        elif player == "Paper":
            if computer == "Scissors":
                print("You lost! Computer picked Scissors.")
            elif computer == "Rock":
                print("You won! Computer picked Rock.")
                player_score += 1
        elif player == "Scissors":
            if computer == "Rock":
                print("You lost! Computer picked Rock.")
            elif computer == "Paper":
                print("You won! Computer picked Paper.")
                player_score += 1
        else:
            print("That's not a valid play. Check your spelling!")

        print(f"Your score: {player_score}")

        if username in high_scores:
            if player_score > high_scores[username]:
                high_scores[username] = player_score
                print("New high score!")
        else:
            high_scores[username] = player_score
            print("New high score!")

        # Reset player to False so the loop can continue
        player = False
        computer = t[randint(0, 2)]

    save_high_scores()