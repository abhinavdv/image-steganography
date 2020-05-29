import cv2
import numpy as np


img = cv2.imread("a.png", 0)

height, width = img.shape

# for i in range(height):
#     for j in range(width):
#         if(img[i][j] <= 244):
#             img[i][j] += 10
#             print(img[i][j])
#         else:
#             img[i][j] -= 20
#             print(img[i][j])

# cv2.imwrite('b.png', img)
s = "my life"
bin_conv = []

for c in s:

    # convert each char to
    # ASCII value
    ascii_val = ord(c)

    # Convert ASCII value to binary
    binary_val = bin(ascii_val)
    bin_conv.append(binary_val[2:])

a = ''.join(bin_conv))
