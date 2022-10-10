def prime():
    number = int(input("Adjon meg egy számot: "))
    pass

def rps():
    player1 = input("Játékos 1 választása (kő, papír, olló): ")
    player2 = input("Játékos 2 választása (kő, papír, olló): ")

    if player1 == "kő":
        a = 1
    elif player1 == "papír":
        a = 2
    elif player1 == "olló":
        a = 3

    if player2 == "kő":
        b = 1
    elif player2 == "papír":
        b = 2
    elif player2 == "olló":
        b = 3

    if a > b:
        print("Játákos 1 nyert!")
    elif a == 1 and b == 3:
        print("Játékos 1 nyert!")
    elif a == b:
        print("Döntetlen!")
    else:
        print("Játékos 2 nyert!")

def fibonacci():
    number = int(input("Adja meg, hány Fibonacci számot generáéjon le: "))
    a = 1
    b = 1
    c = 0
    sum = 1
    while a <= number:
        print(sum)
        c = b
        b = sum
        sum = c + b
        a += 1

def farmer():
    pass

if __name__ == "__main__":
    rps()
    fibonacci()

