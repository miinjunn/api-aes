import sys
from fungsi_aes import break_input, add_round_key_preRound, subByte, mix_column, key_scheduling, rcon, add_round_key
from shift_row import shift_row


# plain_user = "500000.7RLFXN"
plain_user = sys.argv[1]
key_user = sys.argv[2]

# enkripsi
def encrypt(plaintext, keyword):
    # input to dec
    plain = break_input(plaintext)
    key = break_input(keyword)
    state_preRound, state_preRound_hex = add_round_key_preRound(plain, key)

    new_state = state_preRound
    prev_wk = key

    # all_round
    for i in range(10):
        if i != 9:
            round_subByte = subByte(new_state)
            round_shiftRow = shift_row(round_subByte)
            round_mixColumn = mix_column(round_shiftRow)
            round_whitening_key = key_scheduling(prev_wk, rcon[i])
            round_add_round_key = add_round_key(
                round_mixColumn, round_whitening_key)

            new_state = round_add_round_key
            prev_wk = round_whitening_key
        elif i == 9:
            round_subByte = subByte(new_state)
            round_shiftRow = shift_row(round_subByte)
            round_whitening_key = key_scheduling(prev_wk, rcon[i])
            round_add_round_key = add_round_key(
                round_shiftRow, round_whitening_key)

            new_state = round_add_round_key
            prev_wk = round_whitening_key

    # convert output menjadi hex, lalu add 0 jika hex hanya 1 charakter, ex: 'a' -> '0a'
    cipher_hex = []
    for i in new_state:
        cek = hex(i)[2:]
        if len(cek) == 1:
            cek = '0' + cek
        cipher_hex.append(cek)

    return cipher_hex


all_round = encrypt(plain_user, key_user)
# print(all_round)

cipher = ''
for i in all_round:
    cipher += i

print(cipher)
# print(f"len: {len(cipher)}")

# r10 add round key: [41, 195, 80, 95, 87, 20, 32, 246, 64, 34, 153, 179, 26, 2, 215, 58]
# cipher text: 29 c3 50 5f 57 14 20 f6 40 22 99 b3 1a 2 d7 3a
