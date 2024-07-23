from random import randint

t = ["Rock", "Paper", "Scissors"]
high_scores = {}

def get_user_credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            return [line.strip().split() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def login():
    username, password = get_user_credentials()
    users = read_file("users.txt")

    for user, passw in users:
        if username == user and password == passw:
            print("Login successful!")
            return username

    print("Invalid username or password")
    return None

def register():
    username, password = get_user_credentials()
    users = read_file("users.txt")

    for user, _ in users:
        if username == user:
            print("Username already taken")
            return None

    with open("users.txt", "a") as f:
        f.write(f"{username} {password}\n")

    print("Registration successful!")
    return username

def load_high_scores():
    scores = read_file("high_scores.txt")
    return {user: int(score) for user, score in scores}

def save_high_scores():
    with open("high_scores.txt", "w") as f:
        for user, score in high_scores.items():
            f.write(f"{user} {score}\n")

def play_game(username):
    player_score = 0
    computer_choice = t[randint(0, 2)]

    while True:
        print("Let's play Rock, Paper, Scissors")
        player_choice = input("Rock, Paper, Scissors: ").capitalize()

        if player_choice not in t:
            print("That's not a valid play. Check your spelling!")
            continue

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            print(f"You won! Computer picked {computer_choice}.")
            player_score += 1
        else:
            print(f"You lost! Computer picked {computer_choice}.")

        print(f"Your score: {player_score}")

        if username in high_scores:
            if player_score > high_scores[username]:
                high_scores[username] = player_score
                print("New high score!")
        else:
            high_scores[username] = player_score
            print("New high score!")

        computer_choice = t[randint(0, 2)]
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

def main():
    global high_scores
    high_scores = load_high_scores()

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
                print("Logged in. Access granted.")
                break
        elif choice == "2":
            username = register()
            if username:
                print("Registration complete. You can now login.")
        elif choice == "3":
            return None
        else:
            print("Invalid choice. Please try again.")

    return username

# Call the main function to start the login system
username = main()

if username:
    play_game(username)
    save_high_scores()