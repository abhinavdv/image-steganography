import cv2

def encrypt(image, string):


def decrypt(image):


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
