import os
vast = 0
x = 0
vastnum = 3

print("+----------------------------------------------------+")
print("|    Hei! Haluatko että lasken laskun puolestasi?    |")
print("|    (Kirojoita numero)                              |")
print("|    1 - Kyllä                                       |")
print("|    2 - Ei                                          |")
print("+----------------------------------------------------+")

while x == 0:
    vast = input()
    print("vast:", vast)
    try:
        vastnum = int(vast)
        x = 1
        print("x:", x, "vastnum:", vastnum)

        if vastnum != 1 and vastnum != 2:
            raise

    except:
        x = 0
        print("x", x)
        print("Anna vain kysytty numero!")

if vastnum == 1:
    #os.system('cls')
    print("onnistui")

