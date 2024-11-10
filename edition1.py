import hashlib
import base64

def intro():
    print("=== Welcome to the Capture The Flag (CTF) Simulation! ===")
    print("Your goal is to find all the hidden flags by completing various cybersecurity challenges.\n")
    print("Challenges include password cracking, base64 decoding, and file extraction.")
    print("Solve them to collect flags and win!\n")
    print("Type 'quit' anytime to exit the game.\n")
    print("="*50 + "\n")

# Challenge 1: Password Cracking using Hash
def password_cracking_challenge():
    print("\n--- Challenge 1: Password Cracking ---")
    print("You have intercepted a hashed password! Your job is to crack it.")
    hashed_password = hashlib.md5("secret123".encode()).hexdigest()
    print(f"MD5 hashed password: {hashed_password}")
    
    attempts = 3
    while attempts > 0:
        guess = input(f"Enter your guess ({attempts} attempts left): ").strip()
        if guess == "secret123":
            print("Success! You've cracked the password. Here's your flag: FLAG{CR4CK3D_1T}")
            return True
        else:
            print("Wrong guess, try again.")
            attempts -= 1
    
    print("You've run out of attempts! Moving to the next challenge...\n")
    return False

# Challenge 2: Base64 Decoding
def base64_decoding_challenge():
    print("\n--- Challenge 2: Base64 Decoding ---")
    print("You've intercepted a message, but it's encoded in base64.")
    encoded_message = base64.b64encode("CTF{B4S3_64_DECODED}".encode()).decode()
    print(f"Encoded message: {encoded_message}")
    
    decoded_message = input("Decode the message and enter the flag: ").strip()
    if decoded_message == "CTF{B4S3_64_DECODED}":
        print("Correct! Here's your flag: FLAG{B4S3D_FLAG}")
        return True
    else:
        print("Incorrect decoding!")
        return False

# Challenge 3: Hidden File Extraction (simple simulation)
def file_extraction_challenge():
    print("\n--- Challenge 3: Hidden File Extraction ---")
    print("You've found a suspicious file! It seems like there's a hidden message inside.")
    print("Clue: The message is hidden between the lines of random text.")
    
    file_content = """
    Random data here...
    Some other random stuff...
    FLAG{HIDD3N_1N_PLA1N_S1GHT}
    More random data...
    """
    
    print("Extract the flag hidden inside this file:")
    print(file_content)
    
    extracted_flag = input("Enter the extracted flag: ").strip()
    if extracted_flag == "FLAG{HIDD3N_1N_PLA1N_S1GHT}":
        print("Well done! You successfully extracted the hidden file flag.")
        return True
    else:
        print("Oops! That wasn't the correct flag.")
        return False

# Main CTF game loop
def start_ctf_simulation():
    intro()
    
    # Track user progress
    total_flags = 0
    challenges = [
        password_cracking_challenge,
        base64_decoding_challenge,
        file_extraction_challenge
    ]
    
    # Iterate through each challenge
    for challenge in challenges:
        if challenge():
            total_flags += 1
            print(f"Flag collected! You now have {total_flags} flag(s).\n")
        else:
            print("Moving to the next challenge...\n")
    
    # End of game
    print(f"\n=== CTF Simulation Completed! ===")
    print(f"You collected {total_flags} out of {len(challenges)} flags.")
    if total_flags == len(challenges):
        print("Congratulations! You've won the CTF challenge!")
    else:
        print("Try again to collect all flags and win.")

# Run the CTF Simulation
if __name__ == "__main__":
    start_ctf_simulation()
