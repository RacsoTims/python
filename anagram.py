from random import shuffle
from math import factorial
from AyDictionary import AyDictionary

dictionary = AyDictionary()

# pick a word at random
def draw(word):
    pass


# generate a consectutive sequence that will represent the position of letters
def sequence(word):
    
    return [n for n in range(len(word))]


# create anagrams by moving letters around
def create_anagrams(word):
    
    letters = [x for x in word]
    permutations = []
    
    while len(permutations) < factorial(len(word)):
        
        shuffle(letters)        
        str_word = "".join(letters)
        
        if str_word not in permutations:
            permutations.append(str_word)
    
    return permutations


# calculate the anagrams' scores
def calculate_score(word, permutations):
    
    for anagram in permutations:
        if isinstance(anagram, int):
            continue
        else:
            score = 0
            for letter in anagram:
                offset = abs(word.index(letter) - anagram.index(letter))
                score += offset
            permutations.insert(permutations.index(anagram)+1, score)
    
    return permutations


test = "cat"
result = create_anagrams(test)
print(result)
result1 = calculate_score(test, result)
print(result1)
