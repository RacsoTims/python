# URL: https://projecteuler.net/problem=42


def generate_trianglenumbers(integer):
    triangle_numbers = []
    for x in range(1, integer):
        triangle = (x**2 + x) // 2
        triangle_numbers.append(triangle)
    return triangle_numbers


def calculate_word_value(word):
    value = 0
    for letter in word.lower():
        value += ord(letter) - 96   # ASCII offset
    return value


def check_iftriangular(word_value, triangle_numbers):
    is_triangular = False
    if word_value in triangle_numbers:
        is_triangular = True
    return is_triangular


with open('/home/oscar/projects/python/euler_data/euler_42.txt', 'r') as data:
    for string_of_words in data:
        words = (string_of_words.replace('"', "")).split(",")

triangle_numbers = generate_trianglenumbers(30)
count = 0
triangle_words = []

for word in words:
    get_value = calculate_word_value(word.lower())
    if check_iftriangular(get_value, triangle_numbers):
        triangle_words.append(word.lower())
        count += 1
    else:
        continue

print(count, triangle_words)
