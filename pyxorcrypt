from string import ascii_letters, digits, punctuation
from random import randint
mix = ascii_letters+digits+punctuation


def binary_to_text(binary):
    n = int(binary, 2)
    n = n.to_bytes((n.bit_length()+7)//8, "big").decode()
    return n


def adjust_size(message, key, crypt: bool = False):
    message_binary = ""
    key_binary = ""
    for i in range(len(key)):
        c = bin(ord(message[i])).replace("b", "")
        ck = bin(ord(key[i])).replace("b", "")
        if len(c) % 8:
            if len(c) - 8 < 0:
                c = "0" * (8 - len(c)) + c

            else:
                c = "0" * (16 - len(c)) + c

        if len(ck) % 8:
            if len(ck) - 8 < 0:
                ck = "0" * (8 - len(ck)) + ck

            else:
                ck = "0" * (16 - len(ck)) + ck

        message_binary += c
        key_binary += ck

    if crypt:
        return key_binary

    return message_binary, key_binary


def xor(a, b):
    output = ""
    for k, m in zip(a, b):
        if k != m:
            output += "1"

        else:
            output += "0"

    return output


def encrypt(message=""):
    k = "".join([mix[randint(0, len(mix) - 1)] for i in range(len(message))])
    msg_b, key_b = adjust_size(message, k)
    output = xor(msg_b, key_b)
    return output, k


def decrypt(cipher="", key=""):
    key_b = adjust_size(cipher, key, crypt=True)
    output = xor(cipher, key_b)
    return output


while True:
    choice = input("1) Encrypt\n2) Decrypt\n").replace(" ", "").lower()
    if choice == "1":
        msg = input("Message to encrypt> ")
        encrypted_msg, key = encrypt(message=msg)
        print("Encrypted message: " + encrypted_msg)
        print("Key: " + key)

    elif choice == "2":
        msg = input("Binary to decrypt> ")
        key = input("Key> ")
        decrypted_msg = decrypt(cipher=msg, key=key)
        print("Decrypted message: " + binary_to_text(decrypted_msg))

