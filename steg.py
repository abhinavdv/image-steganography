import cv2
import numpy as np
import random


def strToBinary(s):
    bin_conv = []

    for c in s:

        # convert each char to
        # ASCII value
        ascii_val = ord(c)

        # Convert ASCII value to binary
        binary_val = bin(ascii_val)
        bin_conv.append(binary_val[2:])

    return (''.join(bin_conv))


def encrypt(image, string):
    to_be_appended = "01010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101"
    img = cv2.imread(image, 0)
    _bin = strToBinary(string)
    bin_of_str = str(_bin)
    total_size = 256 + len(bin_of_str)
    bin_to_append = to_be_appended + bin_of_str + to_be_appended
    height, width = img.shape
    size = height * width
    rand_no = random.randrange(0, size - total_size - 5, 1)
    row = rand_no // width
    col = rand_no % width

    for i in range(height):
        for j in range(width):
            if(i >= row and j >= col and len(bin_to_append) != 0):
                if((bin_to_append[0] == '1' and img[i][j] % 2 == 0) or (bin_to_append[0] == '0' and img[i][j] % 2 == 1)):
                    if(img[i][j] == 255):
                        img[i][j] -= 1
                    else:
                        img[i][j] += 1
    return 1


if __name__ == "__main__":
    e_or_d = int(input('''Do you want to encrypt or decrypt?
        press 1 to ENCRYPT
        press 2 to DECRYPT

        '''))
    if e_or_d == 1:
        image = input("Please enter the image you want to encrypt your message in.. : ")
        string = input("please enter the message you want to encrypt : ")
        a = encrypt(image, string)
        if(a):
            print("Sucessfully encrypted!!")
        else:
            print("some error")

    elif e_or_d == 2:
        image = input("Please enter the image you want to decrypt your message from.. : ")
        a = decrypt(image)
    else:
        print("Please restart and type in either 1 to encrypt or 2 to decrypt")
