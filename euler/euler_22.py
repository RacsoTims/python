# URL: https://projecteuler.net/problem=22

# PROBLEM: Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# What is the total of all the name scores in the file?

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")
import utils

# read contents of file
names = []
string_names = ""
names_temp = [] # convert string of names to list of names
path = utils.determine_path()


def get_content(string_names):
    with open(f"{path}euler_22.txt") as temp:
        for line in temp:
            string_names += line
    return convert_to_Singlelist(string_names)


def convert_to_Singlelist(string_names):
    names_temp = ((string_names.replace('"', "")).lower()).split(",")
    return names_temp


def calculate_name_score(name, position):
    score = 0
    for char in name:
        score += (ord(char) - ord("a") + 1) # ord("a") = 97
    return score * position


names = get_content(string_names)
names.sort()   # sorted list of all the names

total = 0
for i in range(0, len(names)):
    total += calculate_name_score(names[i], i+1)

print(f"Total: {total}")
