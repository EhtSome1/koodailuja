import os
from pythonKonsoliLaskinOliot import *

vast = 0
x = 0
vastnum = 3
kieli = 0
vastkieli = 0
laskuvast = 0


print("+-------------------------+")
print("|    Language / Kieli     |")
print("|                         |")
print("|    1 - Suomi            |")
print("|    2 - English          |")
print("+-------------------------+")

kieli = checkIfNumber(1,2,"def")

os.system("cls")

x = 0
if kieli == 1:
    print("+----------------------------------------------------+")
    print("|    Hei! Haluatko että lasken laskun puolestasi?    |")
    print("|                                                    |")
    print("|    1 - Kyllä                                       |")
    print("|    2 - Ei                                          |")
    print("+----------------------------------------------------+")

    vast = checkIfNumber(1,2,"fin")

    if vast == 1:
        os.system('cls')
        #print("onnistui")

        print("+--------------------------+")
        print("|    Minkälainen lasku?    |")
        print("|                          |")
        print("|    1 - Pluslasku         |")
        print("|    2 - Miinuslasku       |")
        print("|    3 - Kertolasku        |")
        print("|    4 - Jakolasku         |")
        print("|    5 - neliöjuuri        |")
        print("|    6 - Pinta-ala         |")
        print("|    7 - Prosenttilasku    |")
        print("+--------------------------+")
        
        laskuvast = checkIfNumber(1,7,"fin")


        os.system('cls')

        match laskuvast:
            case 1:
                PlusL()