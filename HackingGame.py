import random
import time

# Simulated user database and tools
users = {}
tools = {
    'phishing_tool': "A tool to create phishing emails.",
    'sql_injection_tool': "A tool to exploit SQL vulnerabilities.",
    'payload_creator': "Create custom payloads for attacks."
}

# Player score
score = 0

def register_user(username, password):
    if username in users:
        return "Username already exists!"
    else:
        users[username] = password
        return "User registered successfully!"

def login_user(username, password):
    return username in users and users[username] == password

def display_tools():
    print("\nAvailable Hacking Tools:")
    for tool, description in tools.items():
        print(f"  - {tool}: {description}")

def execute_command(command):
    global score
    if command == "exit":
        print("Exiting terminal...")
        return False
    elif command in tools:
        print(f"\nExecuting {command}...\n")
        time.sleep(1)  # Simulate processing time
        if command == 'phishing_tool':
            score += create_phishing_email()
        elif command == 'sql_injection_tool':
            score += perform_sql_injection()
        elif command == 'payload_creator':
            score += create_payload()
    else:
        print("Command not found. Type 'exit' to leave the terminal.")
    print(f"Your current score: {score}")
    return True

def create_phishing_email():
    target_email = input("Enter target email: ")
    email_content = input("Enter your phishing email content: ")
    print(f"Phishing email sent to {target_email} with content:\n{email_content}")
    return random.randint(1, 10)  # Random score for the challenge

def perform_sql_injection():
    print("Simulating SQL Injection...")
    print("Target database: users")
    print("Attempting to exploit vulnerability...")
    time.sleep(2)  # Simulate delay
    success = random.choice([True, False])
    if success:
        print("SQL Injection successful! Gained access to user data.")
        return random.randint(5, 15)  # Random score for success
    else:
        print("SQL Injection failed! Detected by security measures.")
        return 0  # No score for failure

def create_payload():
    payload_name = input("Enter the name of your payload: ")
    payload_code = input("Enter your payload code: ")
    print(f"Payload '{payload_name}' created with code:\n{payload_code}")
    return random.randint(1, 5)  # Score for creating a payload

def main():
    print("Welcome to the Black Hat Simulation Game!\n")
    while True:
        print("\n=== Main Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(register_user(username, password))
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login_user(username, password):
                print("Login successful! Welcome to your terminal.")
                while True:
                    display_tools()
                    command = input("Type a command: ")
                    if not execute_command(command):
                        break
            else:
                print("Invalid username or password.")
        
        elif choice == '3':
            print("Exiting game...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
