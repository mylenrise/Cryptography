import pickle
import binascii
import os

from paddingoracle import BadPaddingException, PaddingOracle

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


def is_addition_correct(text):
    value=text[24:]
    amount=int(value, base=2)
    for i in range(amount):
        if tex[8*(31-i):8*(32-i)]!=value:
            return False
    return True


key="E814A693E0E4C9D1EEFDC59547AB71BE"

c1=[]
for j in range(4):
    for i in range(1,9):
        c1.append(toBits(str(i)))
c1.pop()
c1.append('00000000')
res="".join(c1)
print(res)
#ИСХОДНЫЙ ТЕКСТ 5A

def generate(block,byte,last):
    list = []
    for i in range(255):
        if(i<16):
            list.append('0'*(byte*2-1) + str(hex(i)).upper()[2] + last+block)
        else:
            list.append('0' * (byte*2-2) + str(hex(i)).upper()[2:] + last + block)
    for el in list:
        print(el)

block='07A37A3631F6B5EFAA93843BDDD34FB4'
generate (block,1,"60DEE4989EB5A08E85BBF037D863AC")

#BF 
#os.startfile('AES_CBC.exe')
#os.startfile(r'c:/Program Files/Mozilla Firefox/firefox.exe')