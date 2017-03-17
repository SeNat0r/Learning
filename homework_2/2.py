lst = []
n = 0
print('Введите список чисел. \n Чтобы закончить ввод введите "stop"')
while True:
    n = input('Число: ')
    if n != 'stop':
        lst.append(int(n))
    else:
        break

# lst = [1, 2, 3, 4, 5, 6, 7, 89, 45, 11]
# i = 0
# i2 = len(lst) - 1
# r = 0
# for x in lst:
#     r += 1
#     if r <= (len(lst) // 2):
#         lst[i] = lst[i2]
#         # print(lst[i])
#         lst[i2] = x
#         # print(lst[i2])
#         i += 1
#         i2 -= 1
#     else:
#         break
# print(lst)

for i in range(len(lst) // 2):
    lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]

print(lst)
