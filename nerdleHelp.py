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

def main():
    bank = initDict()
    print(str(bank) + "\n")
    bank = removeNum(5, bank)
    print(str(bank) + "\n")
    bank = removeSymbol('*', bank)
    print(str(bank) + "\n")

main()