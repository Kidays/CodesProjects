import cv2 as cv
import sys
img = cv.imread('Python/Lena.png')
# cv.imshow('Displaywindow',img)
# k=cv.waitKey(0)
# if k==ord('s'):
# cv.imwrite('Lena1.png',img)
# ---------------------------------
# import numpy as np
# cap=cv.VideoCapture(0)
# while(True):
#     ret,frame=cap.read()
#     cv.imshow('frame',frame)
#     if cv.waitKey(30)&0xFF==ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()
# ---------------------------------
# (h, w) = img.shape[:2]
# (B, G, R) = cv.split(img)
# cv.imshow('shapes', img)
# cv.imshow('Blue', B)
# cv.imshow('Green', G)
# cv.imshow('Red', R)
# merge_img = cv.merge([B, G, R])
# cv.imshow('Merged BGR', merge_img)
# cv.waitKey()
# ---------------------------------
print('Image shape:', img.shape)
(h, w) = img.shape[:2]
print('height={},width={}'.format(h, w))
print('(B,G,R)=', img[0, 0])
print('(B,G,R)=', img[64, 128])
(cX, cY) = (w//2, h//2)
top_left = img[0:cY, 0:cX]
cv.imshow('top_left', top_left)
bottom_left = img[cY:h, 0:cX]
img[cY:h, 0:cX] = [255, 0, 0]
cv.imshow('bottom_left', bottom_left)
top_right = img[0:cY, cX:w]
img[0:cY, cX:w] = [0, 255, 255]
cv.imshow('top_right', top_right)
bottom_right = img[cY:h, cX:w]
cv.imshow('bottom_right', bottom_right)
cv.waitKey()
# ----------------------------------
