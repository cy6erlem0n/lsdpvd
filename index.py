import block3x3 as bl

choice = int(input('Hello! Select feature: \n1 - Coding. \n2 - Decoding\n'))
if choice == 1:
    way = input('Enter the full path of your image:\nExample: /home/colorlemon/Pk/Devolp/Python/Projekt/diplom/beta0.png\n')
    eway = input('Enter the full path for the new image:\nExample: /home/colorlemon/Pk/Devolp/Python/Projekt/diplom/image2.png\n')
    message = input('Enter your message:\n')
    print('Wait..')
    l = bl.codimg(way, message, eway)
    print(f'Successfully. Your key 1 = {l[0]}, key 2 = {l[1]}')
elif choice == 2:
    way = input('Enter the full path of your image:\nExample: /home/colorlemon/Pk/Devolp/Python/Projekt/diplom/beta0.png\n')
    key1 = int(input('Enter your key 1: '))
    key2 = int(input('Enter your key 2: '))
    print('Wait..')
    message = bl.decodimg(way, key1, key2)
    print( f'Successfully\nYour message:\n{message}')
else:
    print('Incorrect input!!!')