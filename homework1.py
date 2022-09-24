def commands(name):
    name = str(name.lower())

    dict = {}
    for x in name:
        keys = dict.keys()
        if x in keys:
            dict[x] += 1
        else:
            dict[x] = 1
    print(dict)

    print("Fordítva: ", name[-1::-1])

    list = (name.split(" "))
    print("Listába rendezve szavanként: ", list)


if __name__ == "__main__":
    sentence = input("Adjon meg egy mondatot: ")
    commands(sentence)
