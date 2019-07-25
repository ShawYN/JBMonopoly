import cv2 as cv
import os


img = cv.imread('Resources/graphics/Game_UI/Setting_Selected.png',-1)

imgresize = cv.resize(img, (0, 0), fx=0.65, fy=0.65)

#imgresize = cv.resize(img, (1280, 720))

cv.imwrite('Resources/graphics/Game_UI/Setting_Selected_0.65.png',imgresize)