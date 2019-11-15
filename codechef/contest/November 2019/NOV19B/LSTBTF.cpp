#changes c++ code to python for big integer and use strings
#partially correct

import math

def digitSquareSum(numberInString):
    number = 0
    for j in str(numberInString):
        number += int(j) ** 2
    return number
    
def isPerfect(number):
    return number == int(math.sqrt(number) + 0.5) ** 2

def beauty(digit):
    for i in range(int("1" * digit), int("9" * digit)+1):
        if isPerfect(digitSquareSum(i)) and "0" not in str(i):
            return i
    return -1

testCases =int(input())
for testCase in range(testCases):
    digit = int(input())
    print(beauty(digit))
