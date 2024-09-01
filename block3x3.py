import config, cv2 as cv

#функция шифрования
def codes(image3 = [], message = ''):
    a = config.heartrepl(config.bins(image3[1][1]),message)
    b = config.diff_d(a, image3)
    c = config.tablet(b)
    c[2] = config.messInDec(message)
    b = config.sumd(c[0], c[2])
    c = config.plusHeart(a, b)
    b = config.group(c, a)
    return b.tolist()

#функция дешифрования
def decodes(image = []):
    a = config.diff_d(image[1][1],image)
    b = config.tablet(a)
    c = config.diffd(a, b[0])
    a = config.bins(int(image[1][1]))
    b = a[-3:] + config.decs(c)
    return b

#зашифрование
def codimg(way, mess, eway):
    mess = config.rimess(config.textToBits(mess))
    message = mess[0]
    img = config.getrcomafri(way)
    imgr = img[:,:,2]
    l = len(message)//27
    count = 0
    for j in range(0, len(imgr) - 3 + 1, 3):
        if count < l:
            for i in range(0,len(imgr[j]) - 3 + 1, 3):
                if count < l:
                    s = count * 27
                    e = (count + 1 ) * 27
                    line1 = [[],[],[]]
                    for y in range(3):
                        line = []
                        for x in range(3):
                            line.append(int(imgr[j + y][i + x]))
                        line1[y]= line
                    q = codes(line1,message[s:e])
                    for y in range(3):
                        for x in range(3):
                            imgr[j + y][i + x] = int(q[y][x])
                    count += 1
                else:
                    break
        else:
            break
    img[:,:,2] = imgr
    cv.imwrite(eway,img)   
    return l, mess[1]

#розшифрование
def decodimg(way, l = 0, m = 0):
    img = config.getrcomafri(way)
    imgr = img[:,:,2]
    message = ''
    count = 0
    for j in range(0, len(imgr) - 3 + 1, 3):
        if count < l:
            for i in range(0,len(imgr[j]) - 3 + 1, 3):
                if count < l:
                    line1 = [[],[],[]]
                    for y in range(3):
                        line = []
                        for x in range(3):
                            line.append(int(imgr[j + y][i + x]))
                        line1[y]= line
                    message += decodes(line1)
                    count += 1
                else:
                    break
        else:
            break
    message = config.textFromBits(message[:-m])
    return message