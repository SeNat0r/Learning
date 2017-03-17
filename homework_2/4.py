def bn(dec_num):
    bin_num = ""
    while dec_num > 0:
        srvs = dec_num / 2
        dec_num //= 2
        if dec_num == srvs:
            bin_num = "0" + bin_num
        else:
            bin_num = "1" + bin_num
    return bin_num


def dn(bin_num):
    dec_number = 0
    for n in range(len(bin_num)):
        dec_number += int(bin_num[len(bin_num) - 1 - n]) * (2 ** n)
    return dec_number


action = int(input('1: Dec to Bin, 2: Bin to Dec\n'))
if action == 1:
    d = int(input('Введите десятичное число: '))
    print(bn(d))
elif action == 2:
    b = input('Введите двоичное число: ')
    print(dn(b))
