import os



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

def checkIfNumber( kieli):
    while True:
        inputted = input()
        match kieli:
            case "fin":
                try:
                    test = int(inputted)
                    return test
                except ValueError:
                    print("Anna vain numeromerkkejä!")
            
            case "eng":
                try:
                    test = int(inputted)
                    return test
                except ValueError:
                    print("Only give numbers!")

def PlusL():
    os.system('cls')
    numberlist = []
    vast = 1
    print('Anna numero joka lisätään tai kirjoita "0" jtta lasketaan kaikki yhteen (numero)')
    while vast != 0:
        vast = checkIfNumber("fin")

        if vast != 0:
            numberlist.append(vast)
        if vast == 0:
            print("Tulos:", sum(numberlist))