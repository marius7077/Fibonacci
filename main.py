def ask_check_input():
    while True:
        try:
            number = int(input("Entrez le nombre de nombres à afficher : "))
            return number
        except:
            print(f'{number} n\'est pas un nombre')


if __name__ == '__main__':
    _number = ask_check_input()
    fibonacci = [0, 1]
    for i in range(int(_number)):
        fibonacci.append(sum(fibonacci[-2:]))
    print(f'Les {_number} premiers nombres de la suite de fibonacci sont : {fibonacci}')
