from random import randint

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]
player = False

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
                    return True
            except ValueError:
                print("Invalid user data format in the file.")
                return False

    # Display an error message
    print("Invalid username or password")
    return False


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
                    return False
            except ValueError:
                print("Invalid user data format in the file.")
                return False

    # Write the username and password to the text file
    with open("users.txt", "a") as f:
        f.write(f"{username} {password}\n")

    print("Registration successful!")
    return True



def main():
    while True:
        print("Welcome to the login system!")
        print("Choose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            if login():
                # Perform logged-in operations
                print("Logged in. Access granted.")
                break  # Exit the loop after successful login
        elif choice == "2":
            if register():
                # Perform post-registration operations
                print("Registration complete. You can now login.")
        elif choice == "3":
            break  # Exit the loop if the user chooses to quit
        else:
            print("Invalid choice. Please try again.")


# Call the main function to start the login system
main()



while player == False:
    print("Let's play Rock, Paper, Scissors")
    player = input("Rock, Paper, Scissors")
    
    if player == computer:
        print("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lost! Computer picked Paper.")
        elif computer == "Scissors":
            print("You won! Computer picked Scissors.")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lost! Computer picked Scissors.")
        elif computer == "Rock":
            print("You won! Computer picked Rock.")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lost! Computer picked Rock.")
        elif computer == "Paper":
            print("You won! Computer picked Paper.")
    else:
        print("That's not a valid play. Check your spelling!")

    # Reset player to False so the loop can continue
    player = False
    computer = t[randint(0, 2)]