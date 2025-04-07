import numpy as np
import cv2
import imageio

text = 'HELLO WORLD'
steps = 10
size_x = 1024
size_y = 512
images= []

img = np.zeros((size_y,size_x,3), np.uint8)

for i in range(steps):
    font                   = cv2.FONT_HERSHEY_DUPLEX
    fontScale              = 1
    fontColor              = ((255/steps)*i,(255/steps)*i,(255/steps)*i)
    thickness              = 1
    lineType               = 1
    text_width, text_height = cv2.getTextSize(text, font, fontScale, lineType)[0]
    print(text_width)
    bottomLeftCornerOfText = (int(size_x/steps*i),int(size_y/2+0.5*text_height))

    cv2.putText(img,text, 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)

    images.append(img)

#Display the image
cv2.imshow("img",img)

#Save image
cv2.imwrite("out.jpg", img)

cv2.waitKey(0)

imageio.mimsave('mygif.gif', images, format='GIF', duration=5)