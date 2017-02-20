def sort(x):
    tmp = x[0]
    for n in x:
        # print('n', n)
        if n >= tmp:
            tmp = n
            # print('tmp', tmp)
    return tmp
lst = [1, 2, 3, 8, 5, 999, -16, 55, 0 ]
lst2 = []
while len(lst) > 0:
    print(sort(lst))
    lst2.insert(0,sort(lst))
    lst.pop(lst.index(sort(lst)))
print(lst2)