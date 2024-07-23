def get_user_credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password


def read_users_file():
    try:
        with open("users.txt", "r") as f:
            users = [line.strip().split() for line in f if line.strip()]
        return users
    except FileNotFoundError:
        return []


def login():
    username, password = get_user_credentials()
    users = read_users_file()

    for user, passw in users:
        if username == user and password == passw:
            print("Login successful!")
            return True

    print("Invalid username or password")
    return False


def register():
    username, password = get_user_credentials()
    users = read_users_file()

    for user, _ in users:
        if username == user:
            print("Username already taken")
            return False

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
                print("Logged in. Access granted.")
                break
        elif choice == "2":
            if register():
                print("Registration complete. You can now login.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


# Call the main function to start the login system
main()