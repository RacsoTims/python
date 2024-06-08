"""
Description:


"""


from math import sqrt


alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', ' '
            ]
encode_alphabet = {}
for i in range(0, 27):
    encode_alphabet[alphabet[i]] = str(i + 10)
decode_alphabet = {v: k for k, v in encode_alphabet.items()}


def encoding(name):
    digits = []
    for letter in name:
        digits.append(encode_alphabet[letter])
    number = int(''.join(digits))**2
    return number


def decoding(number):
    text = []
    sq_number = int(sqrt(number))
    print(sq_number)
    for digit in range(0, len(str(sq_number)) - 1, 2):
        pair = ''.join([str(sq_number)[digit:digit + 2]])
        letter = decode_alphabet[pair]
        text.append(letter)
    return text


choice0 = input("Do you want to encode (e) or decode (d) something?  ")

if choice0 == 'e':
    text = input("  Text:  ")
    print(f"Number:\t{encoding(text)}")

elif choice0 == 'd':
    number = int(input("  Number:  "))
    print("Text:\t", ''.join(decoding(number)))
