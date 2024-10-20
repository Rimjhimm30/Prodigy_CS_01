# Caesar Cipher Encryption/Decryption Program

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97  # Base for uppercase and lowercase letters
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabet characters remain the same
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)  # Decrypting is same as encrypting with negative shift


def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").upper()

    if choice not in ['E', 'D']:
        print("Invalid choice, exiting.")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (an integer): "))

    if choice == 'E':
        result = encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = decrypt(message, shift)
        print("Decrypted message:", result)


if __name__ == "__main__":
    main()
