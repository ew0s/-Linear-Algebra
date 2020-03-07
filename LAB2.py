from math import pi, acos, pow, sqrt


def filling_array():
    array = [float(i) for i in fin.readline().split()]
    return array


def what_board(a, b, c):
    determinant = (a[0] * b[1] * c[2]) - \
                  (a[0] * b[2] * c[1]) + \
                  (b[0] * c[1] * a[2]) - \
                  (b[0] * c[2] * a[1]) + \
                  (c[0] * a[1] * b[2]) - \
                  (c[0] * a[2] * b[1])

    if determinant >= 0:
        return 1
    else:
        return -1


def angle(dir1, dir2):
    skalar_multiply = dir1[0] * dir2[0] +\
                      dir1[1] * dir2[1] +\
                      dir1[2] * dir2[2]

    len_dir1 = sqrt(pow(dir1[0], 2) +
                    pow(dir1[1], 2) +
                    pow(dir1[2], 2))

    len_dir2 = sqrt(pow(dir2[0], 2) +
                    pow(dir2[1], 2) +
                    pow(dir2[2], 2))

    degree = round(acos(skalar_multiply / (len_dir1 * len_dir2)) * 180 / pi, 2)

    return degree


def check(dir_self, dir_other):
    return dir_self[0] * dir_other[1] - dir_self[1] * dir_other[0]


fin = open("input.txt", "r")
fout = open("output.txt", "w")

#DATA
ship = filling_array()
keel = filling_array()
mast = filling_array()
enemy = filling_array()

#Направляющие веткор короблей
ships_direction = keel

enemy_direction = [enemy[0] - ship[0],
                   enemy[1] - ship[1],
                   enemy[2] - ship[2]]

#Определение борта коробля
board = what_board(ships_direction, enemy_direction, [0, 0, 1])

#Опредение угла между пушкой и нормалью коробля
angle_between_ships = angle(ships_direction, enemy_direction)

if 30 <= angle_between_ships <= 150:
    normal = [0, 0, 1]
    angle_between_must = angle(mast, normal)

    
    ch = check(mast, ships_direction)
    if ch * board < 0:
        angle_between_must *= -1

    if abs(angle_between_must) <= 60:

        print(board, file=fout)

        angle_between_ships = 90 - angle_between_ships
        print(angle_between_ships, file=fout)


        print(angle_between_must, file=fout)
        print("тестик", file=fout)

    else:
        print(0, file=fout)

else:
    print(0, file=fout)

fout.close()