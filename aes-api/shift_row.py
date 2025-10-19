# s_matrix = ['63', 'c0', 'ab', '20', 'eb', '2f', '30',
#             'cb', '9f', '93', 'af', '2b', 'a0', '92', 'c7', 'a2']
# s_matrix = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


# rotate sesuai document(kebawah)
def rotate(state):
    temp = []
    for i in range(4):
        for j in range(4):
            temp.append(state[j*4 + i])
    return temp


# rotate_bro = rotate(s_matrix)
# print(rotate_bro)


# shift
def shift(state, n):
    return state[n:]+state[0:n]


def shifting(state):
    shift_r = []
    for i in range(4):
        temp = state[i*4:i*4+4]
        shift_r += shift(temp, i)
    return shift_r


def shifting_inv(state):
    shift_inv = []
    for i in range(4):
        temp = state[i*4:i*4+4]
        shift_inv += shift(temp, -i)
    return shift_inv

# shift_bro = shifting(rotate_bro)
# print(shift_bro)

# rotate balik
# rotate_balik_bro = rotate(shift_bro)
# print(rotate_balik_bro)

# cara kerja shift-row pada kodingan ini:
# rotate-shift-rotate


def shift_row(state):
    rot = rotate(state)
    geser = shifting(rot)
    shiftRow = rotate(geser)
    return shiftRow


def shift_row_inv(state):
    rot = rotate(state)
    geser = shifting_inv(rot)
    shiftRow_inv = rotate(geser)
    return shiftRow_inv


# tes
# r1_shift_row = shift_row(s_matrix)
# print(f"r1 shift-row: {r1_shift_row}")
