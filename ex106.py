while True:
    func = str(input('Função ou biblioteca: '))
    help(func)
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while True:
        if op not in 'SN':
            op = str(input('Opção invalida, digite de novo S ou N.')).strip().upper()
        if op == 'N':
            break
    if op == 'N':
        break