def polyndrom(s):
    s = s.split()
    s = ''.join(s)
    i = len(s) // 2
    if (len(s) % 2) > 0:
        # print(s[:i:-1])
        # print(s[:i])
        if s[:i] == s[:i:-1]:
            print('True')
        else:
            print('False')
    else:
        # print(s[:i - 1:-1])
        # print(s[:i])
        if s[:i] == s[:i-1:-1]:
            print('True')
        else:
            print('False')


s = input()
polyndrom(s)
