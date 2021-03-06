# Author: Alexander Sutter
# Date: April 4, 2022
# Latest Revision: April 4, 2022

def initDict():
    bank = {
        "nums": [0,1,2,3,4,5,6,7,8,9],
        "symbols": ['+', '-', '*', '/', '='],
        "correct": ['', '', '', '', '', '', '', '']
    }

    return bank

def removeNum(num, bank):
    nums = bank.get("nums")
    if num in nums:
        nums.pop(num) #num == numIndex
        bank["nums"] = nums
    else:
        print("number already removed")
    return bank

def removeSymbol(symbol, bank):
    if symbol == '=':
        print("cannot remove = ")
        return bank

    symbols = bank.get("symbols")
    if symbol in symbols:
        for i in symbols:
            if i == symbol:
                symbols.remove(symbol)
                break
        bank["symbols"] = symbols
    else:
        print("symbol already removed")
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
            print(colors, i)
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

def calculate(equation):
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

def compute(guess):
    # print(guess)
    equation = ""
    answer = ""
    for i in range(len(guess)): #seperate guess at =
        if guess[i] == '=':
            equation = guess[:i]
            answer = guess[i+1:]
            break
    
    answer = int(answer)
    equationResult = calculate(equation)

    if answer == equationResult:
        return True
    else:
        return False

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
        if not lengthCheck:
            print("length of colors input is not correct")
        colorCheck = checkColors(colors)
        if not colorCheck:
            print("incorrect color input")
        if lengthCheck and colorCheck:
            valid = True
        else:
            print("Invalid color input try again")
    
    return colors        

def green(value, bank, i):
    correct = bank["correct"]
    correct[i] = value
    bank["correct"] = correct
    
    return bank

def yellow(value, bank, i):
    print("yellow not done yet")

def black(value, bank):
    symbols = ['+', '-', '*', '/', '=']
    digits = [0,1,2,3,4,5,6,7,8,9]

    if value in symbols:
        bank = removeSymbol(value, bank)
    elif value in digits:
        bank = removeNum(value, bank)
    
    return bank

def getPossible(bank, guess, colors):
    for i in range(8):
        value = guess[i]
        color = colors[i]

        if color == 'g':
            bank = green(value, bank, i)
        elif color == 'y':
            bank = yellow(value, bank, i)
        elif color == 'b':
            bank = black(value, bank)
        else:
            print("error in sorting values and their colors")

def main():
    bank = initDict()
    print(str(bank) + "\n")
    guess = getGuess()
    colors = getColors(guess)
    bank = getPossible(bank, guess, colors)
    print(bank)

main()