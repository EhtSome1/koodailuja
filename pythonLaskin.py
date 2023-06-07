import os
vast = 0
x = 0
vastnum = 3
kieli = 0
vastkieli = 0


print("+-------------------------+")
print("|    Language / Kieli     |")
print("|                         |")
print("|    1 - Suomi            |")
print("|    2 - English          |")
print("+-------------------------+")

while x == 0:
    kieli = input()
    #print("vast:", vast)
    try:    # check if inputted symbol is a number, if not ask again
        vastkieli = int(kieli)
        x = 1
        #print("x:", x, "vastnum:", vastnum)

        if vastkieli != 1 and vastkieli != 2:
            raise

    except:
        x = 0
        #print("x", x)
        print("Only giva a asked number! / Anna vain kysytty numero!")
os.system("cls")

x = 0
if vastkieli == 1:
    print("+----------------------------------------------------+")
    print("|    Hei! Haluatko että lasken laskun puolestasi?    |")
    print("|                                                    |")
    print("|    1 - Kyllä                                       |")
    print("|    2 - Ei                                          |")
    print("+----------------------------------------------------+")

    while x == 0:
        vast = input()
        #print("vast:", vast)
        try:    # check if inputted symbol is a number, if not ask again
            vastnum = int(vast)
            x = 1
            #print("x:", x, "vastnum:", vastnum)

            if vastnum != 1 and vastnum != 2:
                raise

        except:
            x = 0
            #print("x", x)
            print("Anna vain kysytty numero!")

    if vastnum == 1:
        #os.system('cls')
        #print("onnistui")

        print("+--------------------------+")
        print("|    Minkälainen lasku?    |")
        print("|                          |")
        print("|    1 - Pluslasku         |")
        print("|    2 - Miinuslasku       |")
        print("|    2 - Kertolasku        |")
        print("|    2 - Kertolasku        |")
        print("|    2 - Kertolasku        |")
        print("|    2 - Kertolasku        |")
        print("|    2 - Kertolasku        |")
        print("+--------------------------+")
