import numpy as nm, cv2 as cv, sys

#функции 3x3
#число = бинарное в строке
def bins(n = 1):
    b = '' 
    if n == 0:
        b = '0'
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    if len(b) == 1:
        b = '00' + b
    elif len(b) == 2:
        b = '0' + b
    return b

#строка бинарное число, строка бинарный месседж = десяточное инт
def heartrepl(b,c):
    b = b[0:-3]
    b += c[0:3]
    return int(b, 2)

#уменьшаемое, двухмерный массив = одномерный массив
def diff_d(a, b):
    arr = []
    for i in b:
        for j in i:
            arr.append(abs(a - j))
    arr.pop(4) 
    return nm.array(arr) 

#одномерный массив = трёхмерный
def tablet (c):
    b = nm.ones((3,8))
    i = 0
    for a in c:
        int(a)
        if 0 <= a and a < 8:
            b[0][i] = 0
            b[1][i] = 3
        elif a >= 8 and a < 16:
            b[0][i] = 8
            b[1][i] = 3
        elif a >= 16 and a < 32:
            b[0][i] = 16
            b[1][i] = 3
        elif a >= 32 and a < 64:
            b[0][i] = 32
            b[1][i] = 3
        elif a >= 64 and a < 128:
            b[0][i] = 64
            b[1][i] = 4
        else:
            b[0][i] = 128
            b[1][i] = 4
        i += 1
    return b

#одномерный массив = одномерный массив
def messInDec(a):
    a = [a[i:i + 3] for i in range(0, len(a), 3)]
    arr = []
    for i in a[1:]:
        arr.append(int(i,2))
    return nm.array(arr)

#одномерный массив, одномерный массив = одномерный массив
def sumd(a, b):
    c = nm.array(a) + nm.array(b)
    return c

#слагаемое, одномерный массив = одномерный массив
def plusHeart(a, b):
    arr = []
    for i in b:
        arr.append(abs(a + i)) 
    return nm.array(arr) 

#одномерный массив, сердце = двумерный массив
def group(c, b):
    d = nm.ones((3,3))
    d[2][2] = c[7]
    d[2][1] = c[6]
    d[2][0] = c[5]
    d[1][2] = c[4]
    d[1][1] = b
    d[1][0] = c[3]
    d[0][2] = c[2]
    d[0][1] = c[1]
    d[0][0] = c[0]
    return d

#одномерный массив, одномерный массив = одномерный массив
def diffd(a, b):
    c = nm.array(a) - nm.array(b)
    return c

#одномерный массив = строка
def decs(a):
    b = ''
    for i in a:
        b+= bins(int(i))
    return b

#функции изображения
def getrcomafri(a):
    img = cv.imread(a, cv.IMREAD_UNCHANGED) 
    if img is None:   
        sys.exit("Could not read the image.")
    return img

#строка = строка
def textToBits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

#строка = строка
def textFromBits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

#cтрока = строка, инт
def rimess(message = ''):
    b = [len(message) % 27, 27 - (len(message) % 27)]
    if b[0] != 0:
        message += '0' * b[1]
    return message, b[1]