#Convertisseur.py
while 1==1:
    Deci = 0
    Bin = 0
    Hexa = 0
    print("Converter by Selwyndir")
    print(" What conversion do you want to make ? DTB, BTD, DTH, HTD, BTH ou HTB")
    print(" H= Hexadecimal B= Binary D= Decimal")
    choice = str(input(">>> "))
    if choice== "DTB":
        print("What decimal number should be converted to binary?")
        Deci = int(input(">>> "))
        Bin=bin(Deci)
        Bin=Bin[2::]
        print(Bin)
        pause = input("Press enter to continue")
    elif choice== "BTD":
        print("What binary number should be converted to decimal?")
        Bin = str(input(">>> "))
        Deci=int(Bin, 2)
        print(Deci)
        pause = input("Press enter to continue")        
    elif choice== "DTH":
        print("What decimal number should be converted to hexadecimal?")
        Deci = int(input(">>> "))
        Hexa=hex(Deci)
        Hexa=Hexa[2::]
        print(Hexa)
        pause = input("Press enter to continue")
    elif choice== "HTD":
        print("What hexadecimal number should be converted to decimal?")
        Hexa = str(input(">>> "))
        Deci=int(Hexa, 16)
        print(Deci)
        pause = input("Appuyer sur enter pour continuer")
    elif choice== "BTH":
        print("What binary number should be converted to hexadecimal?")
        Bin = int(input(">>> "))
        Hexa=hex(Bin)
        Hexa=Hexa[2::]
        print(Hexa)
        pause = input("Press enter to continue")
        
    elif choice== "HTB":
        print("What hexadecimal number should be converted to binary?")
        Hexa = str(input(">>> "))
        Deci=int(Hexa, 16)
        Bin=bin(Deci)
        Bin=Bin[2::]
        print(Bin)
        pause = input("Press enter to continue")
    else:
        print("Error")
