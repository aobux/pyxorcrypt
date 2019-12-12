"""
@author: aobux
"""

from string import ascii_letters, digits, punctuation
from random import randint
mix = ascii_letters+digits+punctuation


def adjust_size(message, key, crypt: bool = False):
    message_binary = ""
    key_binary = ""
    for i in range(len(key)):
        c = bin(ord(message[i])).replace("b", "")
        ck = bin(ord(key[i])).replace("b", "")

        def adjust(binary):
            out = ""
            if len(binary) % 8:
                if len(binary) - 8 < 0:
                    out = "0" * (8 - len(out)) + out

                else:
                    out = "0" * (16 - len(out)) + out

            return out

        message_binary += adjust(c)
        key_binary += adjust(ck)

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


def decrypt(binary="", key=""):
    key_b = adjust_size(binary, key, crypt=True)
    output = xor(binary, key_b)
    return output
