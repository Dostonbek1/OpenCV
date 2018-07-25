import numpy as np
import cv2

# black = np.zeros([150,200,1], 'uint8')
# cv2.imshow("Black", black)
# print(black[0,0,:])

ones = np.ones([1500, 2000, 3], 'uint8')
# cv2.imshow("Ones", ones)
print(ones[0,0,:])

# white = np.ones([1500,2000,3], 'uint16')
# white *= (255)
# cv2.imshow("White", white)
# print(white[0,0,:])

a = 0

color = ones.copy()
for i in range(1500):

    for j in range(0,1999):
        b = 0
        c = 0
        if a == 1:
            a = 0
            b = 255
        else:
            a = 1
            c = 255
        color[i,j+a] = (0, b, c)
cv2.imshow("Blue", color)
print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()