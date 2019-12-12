from pyxorcrypt import decrypt, encrypt

while True:
    choice = input("1) Encrypt\n2) Decrypt\n").replace(" ", "").lower()
    if choice == "1":
        msg = input("Message to encrypt> ")
        encrypted_msg, key = encrypt(message=msg)
        print("Encrypted message: " + encrypted_msg)
        print("Key: " + key)
        break

    elif choice == "2":
        msg = input("Binary to decrypt> ")
        key = input("Key> ")
        decrypted_msg = encrypt(binary=msg, key=key)
        print("Decrypted message: " + decrypted_msg)
        break
