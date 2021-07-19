def leiadinheiro(msg):
    while True:
        num = str(input(msg)).strip().replace(',', '.')
        if num.isalpha() or num == '':
            print(f'"{num}" não é um precço valido.')
        elif not num.isalpha() and num != '':
            break
    return float(num)
