def increase(price=0, tax=0, format=False):
    result = price + (price * tax / 100)
    return result if format is False else money(result)


def decrease(price=0, tax=0, format=False):
    result = price - (price * tax / 100)
    return result if format is False else money(result)


def double(price=0, format=False):
    result = price * 2
    return result if not format else money(result)

def half(price=0, format=False):
    result = price / 2
    return result if not format else money(result)

def money(price=0, money='$'):
    return f'{money}{price:>.2f}'.replace(',', '.')

def resume(price=0, tax=10, taxing=5):
    print('-' * 30)
    print('RETURN OF THE VALUE'.center(30))
    print('-' * 30)
    print(f'Price analyzed: \t\t\033[1;33m{money(price)}\033[m')
    print(f'Double of the price: \t\033[1;32m{double(price, True)}\033[m')
    print(f'Half of the price: \t\t\033[1;31m{half(price, True)}\033[m')
    print(f'With {tax}% of increase: \t\033[1;32m{increase(price, tax, True)}\033[m')
    print(f'With {taxing}% of decrease: \t\033[1;31m{decrease(price, taxing, True)}\033[m')
    print('-' * 30)

