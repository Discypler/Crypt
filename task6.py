import task1


def start():
    e, N, c = 17, 29329, 16469
    d = task1.mod(f'{e}**-1', task1.phi(N)) # d = e^-1 (mod phi(N))
    print(f'e={e}, N={N}, c={c}')
    print(f'Сообщение - {c**d % N}')
