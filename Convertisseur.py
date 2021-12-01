#Convertisseur.py
while 1==1:
    Deci = 0
    Bin = 0
    Hexa = 0
    print("Convertisseur par Selwyndir")
    print(" Quelle conversion voulez vous effectuer ? DTB, BTD, DTH, HTD, BTH ou HTB")
    print(" H= Hexadecimal B= Binaire D= Decimal")
    choice = str(input(">>> "))
    if choice== "DTB":
        print("Quelle nombre decimal doit être converti en binaire ?")
        Deci = int(input(">>> "))
        Bin=bin(Deci)
        Bin=Bin[2::]
        print(Bin)
        pause = input("Appuyer sur enter pour continuer")
    elif choice== "BTD":
        print("Quelle nombre binaire doit être converti en decimal ?")
        Bin = str(input(">>> "))
        Deci=int(Bin, 2)
        print(Deci)
        pause = input("Appuyer sur enter pour continuer")        
    elif choice== "DTH":
        print("Quelle nombre decimal doit être converti en hexadecimal ?")
        Deci = int(input(">>> "))
        Hexa=hex(Deci)
        Hexa=Hexa[2::]
        print(Hexa)
        pause = input("Appuyer sur enter pour continuer")
    elif choice== "HTD":
        print("Quelle nombre hexadecimal doit être converti en decimal ?")
        Hexa = str(input(">>> "))
        Deci=int(Hexa, 16)
        print(Deci)
        pause = input("Appuyer sur enter pour continuer")
    elif choice== "BTH":
        print("Quelle nombre binaire doit être converti en hexadecimal ?")
        Bin = int(input(">>> "))
        Hexa=hex(Bin)
        Hexa=Hexa[2::]
        print(Hexa)
        pause = input("Appuyer sur enter pour continuer")
        
    elif choice== "HTB":
        print("Quelle nombre hexadecimal doit être converti en binaire ?")
        Hexa = str(input(">>> "))
        Deci=int(Hexa, 16)
        Bin=bin(Deci)
        Bin=Bin[2::]
        print(Bin)
        pause = input("Appuyer sur enter pour continuer")
    else:
        print("Erreur")
