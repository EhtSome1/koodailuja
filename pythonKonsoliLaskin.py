import os
import time
from pythonKonsoliLaskinOliot import *

vast = 0
x = 0
vastnum = 3
kieli = 0
vastkieli = 0
laskuvast = 0
lasketaan = True


print("+-------------------------+")
print("|    Language / Kieli     |")
print("|                         |")
print("|    1 - Suomi            |")
print("|    2 - English          |")
print("+-------------------------+")

kieli = checkIfNumberRange(1,2,"def")

os.system("cls")

x = 0
if kieli == 1:
    print("+----------------------------------------------------+")
    print("|    Hei! Haluatko että lasken laskun puolestasi?    |")
    print("|                                                    |")
    print("|    1 - Kyllä                                       |")
    print("|    2 - Ei                                          |")
    print("+----------------------------------------------------+")

    vast = checkIfNumberRange(1,2,"fin")

    if vast == 1:
        while lasketaan:
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
            
            laskuvast = checkIfNumberRange(1,7,"fin")


            os.system('cls')

            match laskuvast:
                case 1:
                    PlusL()
                case 2:
                    MinL()
                case 3:
                    KertL()
                case 4:
                    JakoL()
                case 5:
                    NeliJ()
                case 6:
                    os.system('cls')
                    print("+----------------------------+")
                    print("|    Minkälainen Pinta-ala:  |")
                    print("|    1 - Nelikulmio          |")
                    print("|    2 - kolmio              |")
                    print("+----------------------------+")
                    pintaAla = int(input())

                    match pintaAla:
                        case 1:
                            KertL()
                        case 2:
                            kolmA()
                case 7:
                    ProsL()

            time.sleep(2.0)
            print("+--------------------------------+")
            print("|    lasketaanko uusi lasku?     |")
            print("|    1 - Kyllä                   |")
            print("|    2 - Ei                      |")
            print("+--------------------------------+")
            laskVast = checkIfNumberRange(1, 2, "fin")
            if laskVast == 2:
                lasketaan = False