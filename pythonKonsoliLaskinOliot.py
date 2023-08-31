import os



def checkIfNumberRange(minNum, maxNum, kieli):
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

def checkIfNumber(kieli):
    while True:
        inputted = input()
        match kieli:
            case "fin":
                try:
                    test = float(inputted)
                    return test
                except ValueError:
                    print("Anna vain numeromerkkejä!")
            
            case "eng":
                try:
                    test = float(inputted)
                    return test
                except ValueError:
                    print("Only give numbers!")

def checkIfNumberOrWord(word, kieli):
    while True:
        inputted = input()
        match kieli:
            case "fin":
                try:
                    test = float(inputted)
                    return test
                except ValueError:
                    if inputted != word:
                        print('Anna vain numeromerkkejä tai"', word +'!')
            
            case "eng":
                try:
                    test = float(inputted)
                    return test
                except ValueError:
                    if inputted != word:
                        print('Only give numbers or"' + word + '"!')


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

def MinL():
    os.system('cls')
    numberlist = []
    vast = 1
    fvast = 1
    print('Anna numero joka vähennetään tai kirjoita "0" jotta lasketaan kaikki (numero)')
    fvast = checkIfNumber("fin")
    while vast != 0:
        vast = checkIfNumber("fin")

        if vast != 0:
            numberlist.append(vast)
        if vast == 0:
            for x in numberlist:
                fvast = fvast - x
            print("Tulos:", fvast)

def KertL():
    os.system('cls')
    numberlist = []
    vast = 1
    fvast = 1
    a = bool(False)
    print('Anna numero joka kerrotaan tai kirjoita "valmis" jotta lasketaan kaikki')

    while a == False:
        vast = checkIfNumberOrWord("valmis", "fin")

        if vast != "valmis":
            numberlist.append(vast)

        if vast == "valmis":
            a = bool(True)
            for x in numberlist:
                fvast = fvast * x
            print("Tulos:", fvast)

# def JakoL():


# def NeliJ():


# def KolmA():