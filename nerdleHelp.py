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

def checkColors(colors):
    for i in colors:
        if i != 'g' or i != 'y' or i != 'b':
            return False
    
    return True

def precedence(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    return 0

def applyOperation(num1, num2, op):
    if op == "+":
        return num1 + num2
    if op == "-":
        return num1 - num2
    if op == "*":
        return num1 * num2
    if op == "/":
        return num1 / num2

def compute(equation):
    nums = []
    operations = []
    i = 0
    while i < len(equation):
        if equation[i] == " ": # get rid of spaces in our equation
            i += 1
            continue
        elif equation[i] == "(":
            operations.append(equation[i])
        elif equation[i].isdigit(): # get number
            val = 0
            while (i < len(equation)) and equation[i].isdigit():
                val = (val*10)+int(equation[i])
                i += 1
            nums.append(val)
            i -= 1
        elif equation[i] == ")": 
            while len(operations) != 0 and operations[-1] != "(":
                val2 = nums.pop()
                val1 = nums.pop()
                op = operations.pop()
                nums.append(applyOperation(val1, val2, op))
            operations.append(equation[i])
        else:
            while ((len(operations) != 0) and precedence(operations[-1]) >= precedence(equation[i])):
                val2 = nums.pop()
                val1 = nums.pop()
                op = operations.pop()
                nums.append(applyOperation(val1, val2, op))
            operations.append(equation[i])
        i += 1
    while len(operations) != 0:
        val2 = nums.pop()
        val1 = nums.pop()
        op = operations.pop()
        nums.append(applyOperation(val1, val2, op))
    return nums[-1]

def getGuess():
    valid = False
    while not valid:
        guess = input("What is your guess? ")
        
        lengthCheck = checkLength(guess)
        if not lengthCheck:
            print("length does not match")
        equalSign = checkEquals(guess)
        if not equalSign:
            print("equal sign does not match")
        computes = compute(guess)
        if not computes:
            print("does not compute")
        
        if lengthCheck and equalSign and computes:
            valid = True
        else:
            print("Invalid guess input please try again")    
    
    return guess

def getColors(guess):
    colors = ""
    valid = False
    while not valid:
        colors = input("What are the colors (g->green, y->yellow, b->black/gray): \n" + guess + "\n")
        if colors == 'all':
            print("Answer is: " + guess)
            break
        lengthCheck = checkLength(colors)
        colorCheck = checkColors(colors)
        if lengthCheck and colorCheck:
            valid = True
        else:
            print("Invalid color input try again")
    
    return colors        

def main():
    bank = initDict()
    print(str(bank) + "\n")
    guess = getGuess()
    getColors(guess)

main()