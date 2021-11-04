# This task is to introduce arrays/strings/conditions in Python. Also some logical thinking.
# Each of the ? must be replaced with a char, that is unique (so can't be same as on left or right).
import random
def solve_riddle(str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm'
        , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    string = list(str)
    pos = string.index('?')

    for char in string:
        if(char == '?'):
            a = random.randrange(0,24)
            letter = alphabet[a]
            pos = string.index('?')
            string[pos] = letter
            for i in range(len(string) - 1):
                if string[i] == string[i + 1]:
                    b = random.randrange(0, 24)
                    letter2 = alphabet[b]
                    string[i] = letter2
                if string[i] == string[i-1]:
                    c = random.randrange(0, 24)
                    letter3 = alphabet[c]
                    string[i] = letter3


    print(string)
    return string

def run_tests():
    is_correct_solution(solve_riddle("abc?def"))
    is_correct_solution(solve_riddle("abc?de?????"))
    is_correct_solution(solve_riddle("??????"))


def is_correct_solution(solved_str):
    if "?" in solved_str:
        raise RuntimeError("Solution can't contain ?, but was '" + solved_str + "'")

    for i in range(len(solved_str) - 1):
        if solved_str[i] == solved_str[i + 1]:
            raise RuntimeError("Solution can't contain 2 same chars next to eachother, but was '" + solved_str + "'")

run_tests()