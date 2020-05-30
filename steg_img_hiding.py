import cv2
import numpy as np
import random


def encrypt(image1, image2, extension):
    imga1 = cv2.imread(image1, 1)
    imga2 = cv2.imread(image2, 1)
    width = 800
    height = 600
    dimen = (width, height)
    img1 = cv2.resize(imga1, dimen, interpolation=cv2.INTER_AREA)
    img2 = cv2.resize(imga2, dimen, interpolation=cv2.INTER_AREA)
    for i in range(600):
        for j in range(800):
            for k in range(3):
                all_bits1 = format(img1[i][j][k], '08b')
                all_bits2 = format(img2[i][j][k], '08b')
                new_pixel = all_bits1[:4] + all_bits2[:4]
                img1[i][j][k] = int(new_pixel, 2)
    cv2.imwrite('message.png', img1)
    return 1


def decrypt(image):
    img = cv2.imread("message.png", 1)
    width = img.shape[0]
    height = img.shape[1]
    retrived_img = np.zeros((width, height, 3), np.uint8)
    for i in range(width):
        for j in range(height):
            for k in range(3):
                img_to_bin = format(img[i][j][k], '08b')
                retrieved_img_bin = img_to_bin[4:] + chr(random.randint(0, 1) + 48) * 4
                retrived_img[i][j][k] = int(retrieved_img_bin, 2)
    cv2.imwrite('retrived_image.png', retrived_img)


if __name__ == "__main__":
    e_or_d = int(input('''Do you want to encrypt or decrypt?
        press 1 to ENCRYPT
        press 2 to DECRYPT

        :'''))
    if e_or_d == 1:
        image = input("Please enter the main image you want to encrypt your image in.. : ")
        extension = image.split('.')
        image2 = input("please enter the image you want to encrypted : ")
        a = encrypt(image, image2, extension[1])
        if(a):
            print("Sucessfully encrypted one image into another!!")
        else:
            print("some error")

    elif e_or_d == 2:
        image = input("Please enter the image you want to decrypt your image from.. : ")
        a = decrypt(image)
        print("Your image has been decrypted Sucessfully")
        print("Your image has been saved in the same directory as retrived image.png")
    else:
        print("Please restart and type in either 1 to encrypt an image or 2 to decrypt an image")
