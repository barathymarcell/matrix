# coding: utf8

meret = float(input("Adjon meg egy számot és egy mértékegységet (cm/inch):\n"))
egyseg = input()

if egyseg == "cm":
    inch = 0.393700787
    print(inch * meret, " inches")

elif egyseg == "inch":
    cm = 2.54
    print(cm * meret, "cm")

else:
    print("A mértékegység nem megfelelő!")