field_first = [['-']*3 for _ in range(3)]
field_top_row = [" ", 0, 1, 2]
count = 0


def field(x=None, y=None, user_name=None):
    """Нарисует игровое поле"""
    global field_first
    if x == 0 or y == 0 or (x and y):
        if field_first[y][x] != "-":
            print("Эта ячейка занята((")
            return get_x_o(user_name)
        else:
            field_first[y][x] = user_name
    print(*field_top_row)
    for l, i in enumerate(field_first):
        print(l, *i)



def get_x_o(user_name):
    """Получить координаты от игрока"""
    global count
    while True:
        x_pos = input(f"Игрок {user_name}, введите координаты: ").split()
        if len(x_pos) == 2:
            if x_pos[0].isdigit() and x_pos[1].isdigit():
                x, y = map(int, x_pos)
                if 0 <= x < 3 and 0 <= y < 3:
                    count += 1
                    break
                else:
                    print("Введите числа от 0 до 2")
            else:
                print("Введите числа")
        else:
            print("Введите две координаты")

    return field(x=x, y=y, user_name=user_name)


def check(user_name=None):
    """Проверяет победителя"""
    global field_first
    global count
    if field_first[0][0] == field_first[0][1] == field_first[0][2] != '-' or \
            field_first[1][0] == field_first[1][1] == field_first[1][2] != '-' or \
            field_first[2][0] == field_first[2][1] == field_first[2][2] != '-' or \
            field_first[0][0] == field_first[1][0] == field_first[2][0] != '-' or \
            field_first[0][1] == field_first[1][1] == field_first[2][1] != '-' or \
            field_first[0][2] == field_first[1][2] == field_first[2][2] != '-' or \
            field_first[0][0] == field_first[1][1] == field_first[2][2] != '-' or \
            field_first[0][2] == field_first[1][1] == field_first[2][0] != '-':
        print("Игра окончена")
        print(f"{user_name} Выиграл")
        repeat = input("Чтобы начать сначала введите y или n для завершения игры: ")
        if repeat == "y" or repeat == "Y":
            field_first = [['-'] * 3 for _ in range(3)]
            count = 0
            field()
            return get_x_o(user_name="X"), True
        elif repeat == "n" or repeat == "N":
            print("Всего доброго!")
            return False
        else:
            print("Введите корректное значение")
            return check(user_name)

    elif count == 9:
        print("Игра окончена")
        print("Победила дружба!")
        repeat = input("Чтобы начать сначала введите Y или N для завершения игры: ")
        if repeat == "y" or repeat == "Y":
            field_first = [['-'] * 3 for _ in range(3)]
            count = 0
            field()
            return get_x_o(user_name="X"), True
        elif repeat == "n" or repeat == "N":
            print("Всего доброго!")
            return False
        else:
            print("Введите корректное значение")
            return check(user_name)
    return True


