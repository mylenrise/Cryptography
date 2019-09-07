import pickle
import binascii

FILENAME = "text.dat"
with open(FILENAME, "rb") as file:
    text = pickle.load(file)

blockSize = 32
key = "dead"


def toText(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def toBits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def split(text, blockSize):
    blocks = []
    fill = blockSize - len(text) % blockSize
    blocks_amount = len(text) // blockSize
    for i in range(blocks_amount):
        blocks.append(text[i * blockSize:i * blockSize + blockSize])

    blocks.append(text[blocks_amount * blockSize:] + '1' + '0' * (fill - 1))
    return blocks


def XoR(block, key):
    res = ''
    for i in range(len(block)):
        res += str((int)(block[i]) ^ (int)(key[i]))
    return res


# s_encrypt=[0xf,   0x3,   0xa,   0x8,   0x5,   0xd,   0x6,   0xe,   0x4,   0x7,   0xc,   0x9,   0x2,   0x0,   0x1,   0xb]
s_encrypt_table = ['1111', '0011', '1010', '1000', '0101', '1101', '0110', '1110', '0100', '0111', '1100', '1001',
                   '0010', '0000', '0001', '1011']
s_decrypt_table = ['1101', '1110', '1100', '0001', '1000', '0100', '0110', '1001', '0011', '1011', '0010', '1111',
                   '1010', '0101', '0111', '0000']

p_encrypt_table = [3, 23, 17, 9, 21, 19, 2, 15, 24, 16, 14, 25, 30, 26, 11, 28, 8, 27, 29, 22, 1, 31, 7, 10, 18, 5, 0,
                   4, 12, 6, 13, 20]
p_decrypt_table = [26, 20, 6, 0, 27, 25, 29, 22, 16, 3, 23, 14, 28, 30, 10, 7, 9, 2, 24, 5, 31, 4, 19, 1, 8, 11, 13, 17,
                   15, 18, 12, 21]


def s_encrypt(block):
    res = ''
    for i in range(blockSize // 4):
        res += s_encrypt_table[int(block[i * 4:i * 4 + 4], base=2)]
    return res


def s_decrypt(block):
    res = ''
    for i in range(blockSize // 4):
        res += s_decrypt_table[int(block[i * 4:i * 4 + 4], base=2)]
    return res


def p_encrypt(block):
    res = ''
    for i in range(blockSize):
        res += block[p_encrypt_table[i]]
    return res


def p_decrypt(block):
    res = ''
    for i in range(blockSize):
        res += block[p_decrypt_table[i]]
    return res


def delete_fill(block):
    n = len(block) - len(block.rstrip("0"))
    return block[:len(block) - n - 1]


key = toBits(key)


def encrypt():
    blocks = split(toBits(text), blockSize)
    xorBlocks = []
    for block in blocks:
        xorBlocks.append(XoR(block, key))
    subBlocks = []
    for block in xorBlocks:
        subBlocks.append(s_encrypt(block))
    res = []
    for block in subBlocks:
        res.append(p_encrypt(block))
    return res


encrypt_blocks = encrypt()
print("***ENCRYPTION RESULT***")
print(encrypt_blocks)
print()


def decrypt():
    decrypt_temp = []
    for block in encrypt_blocks:
        decrypt_temp.append(XoR(s_decrypt(p_decrypt(block)), key))
    decrypt_temp[len(decrypt_temp) - 1] = (delete_fill(decrypt_temp[len(decrypt_temp) - 1]))
    res = []
    for block in decrypt_temp:
        res.append(toText(block))
    return res


Lenore = ''.join(decrypt())
print("***DECRYPTION RESULT***")
print(Lenore)
if text == Lenore:
    print("\n***DECRYPTION SUCCESSED***")
else:
    print("\n***DECRYPTION FAILED***")
