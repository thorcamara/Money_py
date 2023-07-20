def readMoney(msg):
    valid = False
    while not valid:
        entry = str(input(msg)).replace(',', '.').strip()
        if entry.isalpha() or entry == '':
            print(f'\033[1;31mERROR: \"{entry}\" it is a invalid price!\033[m')
        elif entry.isnumeric():
            valid = True
            return float(entry)
        else:
            print('\033[1;31mERROR! Type a valid Integer.\033[m')

