import sys
from fungsi_aes import break_input, reverse_break, rcon, add_round_key, key_expansion, subByte_inv, mix_column_inv
from shift_row import shift_row_inv

cipher_user = sys.argv[1]
key_user = sys.argv[2]


# dekripsi
def decrypt(ciphertext, keyword):
    cipher = reverse_break(ciphertext)
    key = break_input(keyword)
    wk_round = key_expansion(key, rcon)
    new_state = []

    for i in range(10):
        if i == 0:
            inv_add_round_key = cipher
            inv_shiftRow = add_round_key(inv_add_round_key, wk_round[-(i+1)])
            inv_subByte = shift_row_inv(inv_shiftRow)
            new_state = inv_subByte
        else:
            inv_add_round_key = subByte_inv(new_state)
            inv_mix_column = add_round_key(inv_add_round_key, wk_round[-(i+1)])
            inv_shiftRow = mix_column_inv(inv_mix_column)
            inv_subByte = shift_row_inv(inv_shiftRow)
            new_state = inv_subByte

    ark = subByte_inv(new_state)
    plaintext = add_round_key(ark, wk_round[0])

    # convert output menjadi hex, lalu add 0 jika hex hanya 1 charakter, ex: 'a' -> '0a'
    plaintext_hex = []
    for i in plaintext:
        cek = hex(i)[2:]
        if len(cek) == 1:
            cek = '0' + cek
        plaintext_hex.append(cek)
    return plaintext_hex


all_round = decrypt(cipher_user, key_user)
all_round = [chr(int(i, base=16)) for i in all_round]


plain = ''
for i in all_round:
    plain += i
print(plain)
