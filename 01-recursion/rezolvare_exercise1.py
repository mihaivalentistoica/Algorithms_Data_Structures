number_list = [1, 1, 1, 1]


def suma(number):
    if len(number) == 1:
        return number[0]
    if len(number) == 0:
        return 0
    return number[0] + suma(number[1:])


print(suma(number_list))
