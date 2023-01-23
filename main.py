import numpy as np

s_box = (
    (0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76),
    (0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0),
    (0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15),
    (0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75),
    (0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84),
    (0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF),
    (0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8),
    (0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2),
    (0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73),
    (0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB),
    (0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79),
    (0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08),
    (0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A),
    (0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E),
    (0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF),
    (0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16),
)
r_con = (0x01, 0x02, 0x04, 0x08, 0x10, 0x20,
    0x40,0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D,
    0x9A,0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35,
    0x6A,0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91,
    0x39)

def get_rcon(index):
    r = []
    r.append(hex(r_con[index]))
    r.append(hex(00))
    r.append(hex(00))
    r.append(hex(00))
    return r

def makeMatrix(h):
    arr=np.array(h)
    matrix= arr.reshape(4,4)
    matrix=matrix.transpose()
    # l = [list(i) for i in matrix]
    return matrix

def subByte(s):
        s_b = []
        for i in s:
            r = int(i[2],base=16)
            c = int(i[3],base=16)

            a = s_box[r][c]
            s_b.append(hex(a))

        return s_b

def xor(l1,l2):
    size = len(l1)
    l = []
    for i in range(size):
        a = hex(int(l1[i],base=16) ^ int(l2[i],base=16) )
        if len(a) < 4:
            a = a[:2] + "0" + a[2]
        l.append(a)
    return l

def xor_lists(rows):
    size = len(rows)
    if size < 2:
        return False

    x = xor(rows[0],rows[1])

    if size > 2:
        for i in range(2,size):
            x = xor(x,rows[i])

    return x

def subKey(index,matrix):
    lastCol = matrix[:, 3]


    lastCol = np.concatenate((lastCol[1:], lastCol[:1]))

    sub_byte = subByte(lastCol)
    r = get_rcon(index)


    sub_key = []
    for i,v in enumerate(matrix):
        col = matrix[:, i]
        if i ==0:
            rows = [sub_byte, r, col]
            xor = xor_lists(rows)
            sub_key.append(xor)
        else:
            col0 = sub_key[i-1]
            xor = xor_lists([col0, col])
            sub_key.append(xor)

    sub_key = np.array(sub_key)
    sub_key = sub_key.transpose()

    return sub_key

def keygeneration(keym):

    keys = []
    k = keym
    keys.append(k)
    for i in range(10):
        k = subKey(i,k)
        keys.append(k)

    return  keys
        # print(i,k)

def printMatrix(matrix):
    print("Matrix:")
    for i in matrix:
        print(i)

def shiftRows(matrix):
    m = matrix.tolist()

    def shift(x):
        x.append(x.pop(0))
        return x

    m[1] = shift(m[1])

    m[2] = shift(m[2])
    m[2] = shift(m[2])

    m[3] = shift(m[3])
    m[3] = shift(m[3])
    m[3] = shift(m[3])

    m = np.array(m)
    return m

def mul_binary(firstnumber, secondnumber):
    Multiplication = int(firstnumber, 2) * int(secondnumber, 2)
    return "{0:08b}".format(Multiplication)

def mixColumn(matrix):

    m = [
        ['0x02','0x03','0x01','0x01'],
        ['0x01','0x02','0x03','0x01'],
        ['0x01','0x01','0x02','0x03'],
        ['0x03','0x01','0x01','0x02']
    ]

    m = np.array(m)
    result = np.ones((4, 4),dtype=str)
    for i in range(4):
        for j in range(4):
            bins = []
            for k in range(4):
                bin1 = "{0:08b}".format(int(m[i][k], 16))
                bin2 = "{0:08b}".format(int(matrix[k][j], 16))
                print(bin1,bin2)
                bin3 = mul_binary(bin1,bin2)
                bins.append(bin3)
            # res = "{0:08b}".format(int( int(bins[0],base=2) ^ int(bins[1],base=2) ^ int(bins[2],base=2) ^ int(bins[3],base=2) ))
            print(bins)
            # result[i][j] = (hex(int(res, 2)))


    return result


def add_round_key(state, round_key):
    result = [0 for x in range(4)]

    for i in range(4):
        result[i] = xor(state[i], round_key[i])

    for i in range(4):
        for j in range(4):
            result[i][j] = result[i][j].replace('0x', '')

    return result

def aesDecyption(cipher,final=[]):


    key = open("p.key", "r")
    key = key.read()
    hexkey = []
    for k in key:
        hexkey.append("0x" + k + k)

    keymatrix = makeMatrix(hexkey)
    # printMatrix(keymatrix)
    keys = keygeneration(keymatrix)
    print(keys)

    index=0
    for i in range(48):
        state = cipher[index:index+16]
        # add round key function here


        c = 144
        for j in range(9):
            # inverseShiftRows(state=state)
            # inverseSubBytes(state=state)
            # add round key function here
            c -= 16
            # Inverse Mix columns

        # Final Round
        # inverseShiftRows(state=state)
        # inverseSubBytes(state=state)
        # add round key function here

        final.extend(state)
        index += 16

    return final

def main():
    key = open("p.key", "r")
    key = key.read()
    hexkey = []
    for k in key:
        hexkey.append("0x"+k+k)


    text = open("text.pt", "r")
    text = text.read()

    keymatrix = makeMatrix(hexkey)
    printMatrix(keymatrix)
    keys = keygeneration(keymatrix)

    hextext = []
    for k in text:
        hextext.append("0x" + k + k)

    textmatrix = makeMatrix(hextext)

    print("text Matrix\n")

    sub_byte = []
    for i in textmatrix:
        s = subByte(i)
        sub_byte.append(s)

    s = np.array(sub_byte)



    shifted = shiftRows(s)

    print(shifted)

    mc = mixColumn(shifted)
    print(mc)


main()