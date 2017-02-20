dec = int(input('Введите десятичное число: '))
bin = ""
while dec > 0:
    srvs = dec / 2
    dec = dec // 2
    if dec == srvs:
        bin = "0" + bin
    else:
         bin = "1" + bin
print(bin)
