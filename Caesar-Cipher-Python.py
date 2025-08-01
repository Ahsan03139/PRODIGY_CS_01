def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# ===== Main Program =====
print("=== Caesar Cipher Tool ===")
print("E - Encrypt a message")
print("D - Decrypt a message")

choice = input("Choose an option (E or D): ").upper()

if choice == "E":
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter shift value: "))
    encrypted_msg = encrypt(message, shift)
    print(f"\nEncrypted Message: {encrypted_msg}")

elif choice == "D":
    message = input("Enter the message to decrypt: ")
    shift = int(input("Enter shift value used during encryption: "))
    decrypted_msg = decrypt(message, shift)
    print(f"\nDecrypted Message: {decrypted_msg}")

else:
    print("Invalid choice! Please enter E or D.")
