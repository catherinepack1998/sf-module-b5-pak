import tic_engine as t

user_x = "X"
user_o = "O"
print("Игрок Х ходит первым")
t.field()
while True:
    t.get_x_o(user_x)
    if not t.check(user_x):
        break
    t.get_x_o(user_o)
    if not t.check(user_o):
        break
