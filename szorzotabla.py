if __name__ == '__main__':
    szorzotabla = int(input('Milyen nagy legyen a szorzótábla?'))

    tabla = '{:>3}{:>6}' + ('{:>4}' * (szorzotabla - 1))
    szamok = list(range(1,szorzotabla+1))

    print(tabla.format('', *szamok))
    print('   :------' + ('----' * (szorzotabla - 1)))

    for num in szamok:
        output = [str(num) + ':']
        for szorzo in szamok:
            output.append(num * szorzo)
        print(tabla.format(*output))