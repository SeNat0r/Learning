from datetime import date


def ny():
    # print(date.today())
    # print(date.today().year)
    delta = date(date.today().year + 1, 1, 1) - date.today()

    return delta.days


# print('До нового года осталось {} дней'.format(ny()))
print('До нового года', ny(), 'дней')