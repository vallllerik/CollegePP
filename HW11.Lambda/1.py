while True:
    name = input()
    if name != 'off':
        a = lambda name_, word: print(name_, word)
        a(name, 'гений')
    else:
        break