from sys import argv

script, input_file = argv

def print_all(f): # function for opening and reading a file
    print(f.read())

def rewind(f): # function for rewinding, i.e., setting the 'read head' to some position in the file (to the beginning when x = 0 for seek(x))
    f.seek(0)

def print_a_line(line_count, f): # function for printing the number corresponding to the current line, and the content of that line
    print(line_count, f.readline(), end = "") # 'readline()' gives the content of the line the 'read head' is currently on

current_file = open(input_file)

print("First, let's print the whole file:\n")

print_all(current_file)

print("Now, let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) # 'current_line' refers to the nth line relative to the position of the 'read head', not the nth line of the file itself

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
