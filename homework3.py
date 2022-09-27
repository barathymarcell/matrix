def haromszog():
    print("Adja meg a háromszög A oldalát:")
    a = input()
    print("Adja meg a háromszög B oldalát:")
    b = input()
    print("Adja meg a háromszög C oldalát:")
    c = input()

    if a + b > c:
        if a + c > b:
            if b + c > a:
                print("A háromszög megfelelő")
    else:
        print("A háromszög nem megfelelő")

if __name__ == '__main__':
    haromszog()