import os

vast = ""

def checkIfNumber(minNum, maxNum, kieli):
    while True:
        inputted = input()
        match kieli:
            case "def":
                try:
                    test = int(inputted)
                    if minNum <= test <= maxNum:
                        return test
                    else:
                        print("Anna luku alueelta / Give a number in the range of", minNum, "-", maxNum)
                except ValueError:
                    print("Anna vain numeromerkkejä! / Only give numbers!")

            case "fin":
                try:
                    test = int(inputted)
                    if minNum <= test <= maxNum:
                        return test
                    else:
                        print("Anna luku alueelta", minNum, "-", maxNum)
                except ValueError:
                    print("Anna vain numeromerkkejä!")
            
            case "eng":
                try:
                    test = int(inputted)
                    if minNum <= test <= maxNum:
                        return test
                    else:
                        print("Give a number in the range of", minNum, "-", maxNum)
                except ValueError:
                    print("Only give numbers!")

def PlusL():
    os.system('cls')
    numberlist = []

    while vast != 0:
        print('Anna numero joka lisätään tai kirjoita "0" (numero)')
        vast = checkIfNumber()

        if vast != 0:
            numberlist.append(vast)