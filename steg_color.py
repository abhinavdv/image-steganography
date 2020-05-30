import cv2
import numpy as np
import random


def BinaryToDecimal(binary):
    string = int(binary, 2)
    return string


def strToBinary(string):
    bin_conv = []
    for char in string:
        ascii_val = ord(char)
        if(ascii_val < 64):
            bin_conv.append('0')
        binary_val = bin(ascii_val)
        bin_conv.append(binary_val[2:])
    return (''.join(bin_conv))


def encrypt(image, string, extension):
    to_be_appended = "11111111111111111111111111111111111111111111111111111111111111111111111111111111100000000000011111111111111111111111111111111110"
    img = cv2.imread(image, 1)
    b, g, r = cv2.split(img)
    _bin = strToBinary(string)
    bin_of_str = str(_bin)
    total_size = 256 + len(bin_of_str)
    bin_to_append = to_be_appended + bin_of_str + to_be_appended
    height, width, _tr = img.shape
    size = height * width
    rand_no = random.randrange(0, height - 12, 1)
    row = rand_no
    t = ''
    for i in range(row, height):
        for j in range(width):
            if(len(bin_to_append) != 0):
                if((bin_to_append[0] == '1' and b[i][j] % 2 == 0) or (bin_to_append[0] == '0' and b[i][j] % 2 == 1)):
                    if(b[i][j] == 255):
                        b[i][j] -= 1
                        t = t + str((b[i][j] % 2))

                    else:
                        b[i][j] += 1
                        t = t + str((b[i][j] % 2))
                bin_to_append = bin_to_append[1:]

    imag = cv2.merge((b, g, r))
    cv2.imwrite('abc.' + extension, imag)
    if(len(bin_to_append) == 0):
        return 1
    else:
        return 0


def decrypt(image):
    appended_front_and_back = "11111111111111111111111111111111111111111111111111111111111111111111111111111111100000000000011111111111111111111111111111111110"
    img = cv2.imread(image, 1)
    b, g, r = cv2.split(img)
    height, width, _sd = img.shape
    a = ""
    for i in range(height):
        for j in range(width):
            a = a + str(b[i][j] % 2)
    print(a.count(appended_front_and_back))
    start_index = a.find(appended_front_and_back)
    start_index = start_index + 128
    a = a[start_index:]
    end_index = a.find(appended_front_and_back)
    a = a[0:end_index]
    str_data = ''

    for i in range(0, len(a), 7):
        temp_data = a[i:i + 7]
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    return(str_data)


if __name__ == "__main__":
    e_or_d = int(input('''Do you want to encrypt or decrypt?
        press 1 to ENCRYPT
        press 2 to DECRYPT

        :'''))
    if e_or_d == 1:
        image = input("Please enter the image you want to encrypt your message in.. : ")
        extension = image.split('.')
        string = input("please enter the message you want to encrypt : ")
        a = encrypt(image, string, extension[1])
        if(a):
            print("Sucessfully encrypted!!")
        else:
            print("some error")

    elif e_or_d == 2:
        image = input("Please enter the image you want to decrypt your message from.. : ")
        a = decrypt(image)
        print("Your message has been decrypted Sucessfully")
        print("Your message is: " + a)
    else:
        print("Please restart and type in either 1 to encrypt or 2 to decrypt")
