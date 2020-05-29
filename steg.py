import cv2
import numpy as np


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
    img = cv2.imread(image, 0)
    bin_of_str = strToBinary(string)

    height, width = img.shape
    for i in range(height):
        for j in range(width):
            if(img[i][j] <= 244):
                img[i][j] += 10
                print(img[i][j])
            else:
                img[i][j] -= 20
                print(img[i][j])


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
