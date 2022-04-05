# Author: Alexander Sutter
# Date: April 4, 2022
# Latest Revision: April 4, 2022

def initDict():
    bank = {
        "nums": [0,1,2,3,4,5,6,7,8,9],
        "symbols": ['+', '-', '*', '/', '='],
    }

    return bank

def removeNum(num, bank):
    nums = bank.get("nums")
    nums.pop(num) #num == numIndex
    bank["nums"] = nums
    return bank

def removeSymbol(symbol, bank):
    if symbol == '=':
        print("cannot remove = ")
        return bank

    symbols = bank.get("symbols")
    for i in symbols:
        if i == symbol:
            symbols.remove(symbol)
            break
    bank["symbols"] = symbols
    return bank

def checkLength(guess):
    if len(guess) == 8:
        return True
    else: 
        print("invalid guess (incorrect length)!")
        return False

def checkEquals(guess):
    symbols = ['+', '-', '*', '/']
    hitEqual = False
    for i in guess:
        if i == '=':
            hitEqual = True
        if hitEqual:
            if i in symbols:
                print("invalid guess (operation after equals)!")
                return False
    if hitEqual:
        return True
    else:
        return False

def compute(check):
    symbols = ['+', '-', '*', '/']
    tempNum = 0
    nums = []
    for i in range(len(check)):
        if i in symbols:
            print("hi")



def getGuess():
    valid = False
    while not valid:
        guess = input("What is your guess")
        lengthCheck = checkLength(guess)
        equalSign = checkEquals(guess)
        computes = compute(guess)
            
    return guess

def main():
    bank = initDict()
    print(str(bank) + "\n")
    print(getGuess())

main()