# ELI5 Python Demo: Public Key Cryptography
# Topic: Showing how the Public Key (Encryption) and Private Key (Decryption) must work together.

# --- 1. Define the Keys (The Best Friends) ---
# In real life, these are complex numbers. Here, they are simple math rules.

PUBLIC_KEY = 3  # The key everyone uses to lock the box (encrypt)
PRIVATE_KEY = 7 # The key only you have to open the box (decrypt)

# A simple mathematical "cipher" to demonstrate the concept.
# Note: This is NOT a secure or real-world algorithm, it is for demonstration only.

def encrypt_message(message, public_key):
    """Locks the message using the Public Key."""
    # We use a simple multiplication rule to 'lock' the message
    locked_message = message * public_key
    print(f"\n--- Encrypting ---")
    print(f"Original Message (Number): {message}")
    print(f"Public Key Used: {public_key}")
    return locked_message

def decrypt_message(locked_message, private_key):
    """Unlocks the message using the Private Key."""
    # We use a simple division rule to 'unlock' the message
    unlocked_message = locked_message // private_key
    print(f"\n--- Decrypting ---")
    print(f"Locked Message: {locked_message}")
    print(f"Private Key Used: {private_key}")
    return unlocked_message

# --- 2. Simulation ---

# The secret message (we are using a number to keep the math simple for ELI5)
SECRET_NUMBER = 21

# Alice locks the box with YOUR Public Key
encrypted = encrypt_message(SECRET_NUMBER, PUBLIC_KEY)

# The Locked Box is sent over the internet (where anyone can see it!)
print(f"SENT OVER INTERNET (The Ciphertext): {encrypted}")


# You unlock the box with YOUR Private Key
decrypted = decrypt_message(encrypted, PRIVATE_KEY)

# --- 3. Result ---
print(f"\nResult: The secret message is: {decrypted}")

# --- What happens if a thief tries to use the WRONG key? ---
print(f"\n--- THIEF ATTACK (using the Public Key to decrypt) ---")
decryption_by_thief = encrypted // PUBLIC_KEY
print(f"Thief's Decryption Attempt: {decryption_by_thief} (Wrong!)")
# The wrong key (PUBLIC_KEY) doesn't unlock the correct message!
