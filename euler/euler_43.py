# URL: https://projecteuler.net/problem=43

import sys
sys.path.append("/home/oscar/tools/")
import utils

divisors = [2, 3, 5, 7, 11, 13, 17]
digits = [str(d) for d in range(0, 10)]


def two_divisible() -> list:
    
    combinations = []
    
    for n in range(10, 1000, 2):
        if n < 100:
            combination = "0" + str(n)
        else:
            combination = str(n)
        
        if utils.repeated_digit(combination):
            combinations.append(combination)
    
    return combinations


def three_divisble(combinations, digits) -> list:
    
    temp_list = []
    
    for combination in combinations:
        for digit in digits:
            temp_string = combination
            if digit in temp_string:
                continue
            else:
                temp_string += digit
                if int(temp_string[1:]) % 3 == 0 and utils.repeated_digit(temp_string):
                    temp_list.append(temp_string)
    
    combinations = temp_list
    
    return combinations


def five_divisble(combinations, digits) -> list:
    
    temp_list = []
    
    for combination in combinations:
        for digit in digits:
            temp_string = combination
            if digit in temp_string:
                continue
            else:
                temp_string += digit
                if int(temp_string[2:]) % 5 == 0 and utils.repeated_digit(temp_string):
                    temp_list.append(temp_string)
    
    combinations = temp_list
    
    return combinations


def seven_divisble(combinations, digits) -> list:
    
    temp_list = []
    
    for combination in combinations:
        for digit in digits:
            temp_string = combination
            if digit in temp_string:
                continue
            else:
                temp_string += digit
                if int(temp_string[3:]) % 7 == 0 and utils.repeated_digit(temp_string):
                    temp_list.append(temp_string)
    
    combinations = temp_list
    
    return combinations


def eleven_divisble(combinations, digits) -> list:
    
    temp_list = []
    
    for combination in combinations:
        for digit in digits:
            temp_string = combination
            if digit in temp_string:
                continue
            else:
                temp_string += digit
                if int(temp_string[4:]) % 11 == 0 and utils.repeated_digit(temp_string):
                    temp_list.append(temp_string)
    
    combinations = temp_list
    
    return combinations


def thirteen_divisble(combinations, digits) -> list:
    
    temp_list = []
    
    for combination in combinations:
        for digit in digits:
            temp_string = combination
            if digit in temp_string:
                continue
            else:
                temp_string += digit
                if int(temp_string[5:]) % 13 == 0 and utils.repeated_digit(temp_string):
                    temp_list.append(temp_string)
    
    combinations = temp_list
    
    return combinations


def seventeen_divisble(combinations, digits) -> list:
    
    temp_list = []
    
    for combination in combinations:
        for digit in digits:
            temp_string = combination
            if digit in temp_string:
                continue
            else:
                temp_string += digit
                if int(temp_string[6:]) % 17 == 0 and utils.repeated_digit(temp_string):
                    temp_list.append(temp_string)
    
    combinations = temp_list
    
    return combinations


def add_remainingDigit(combinations, digits):
    for i in range(0, len(combinations)):
        for digit in digits:
            if digit in combinations[i]:
                continue
            else:
                combinations[i] = digit + combinations[i]
    return combinations


test = two_divisible()
test = three_divisble(test, digits)
test = five_divisble(test, digits)
test = seven_divisble(test, digits)
test = eleven_divisble(test, digits)
test = thirteen_divisble(test, digits)
test = seventeen_divisble(test, digits)
test = add_remainingDigit(test, digits)
print(sum([int(x) for x in test]))
