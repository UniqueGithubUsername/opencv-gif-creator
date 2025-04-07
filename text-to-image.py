import numpy as np
import cv2

# Text
text = 'HELLO WORLD'

# Create a black image
img = np.zeros((512,1024,3), np.uint8)

# Write some Text
#font                   = cv2.FONT_HERSHEY_SIMPLEX
font                   = cv2.FONT_HERSHEY_DUPLEX
fontScale              = 1
fontColor              = (255,255,255)
thickness              = 1
lineType               = 1
text_width, text_height = cv2.getTextSize(text, font, fontScale, lineType)[0]
print(text_width)
bottomLeftCornerOfText = (512-int(0.5*text_width),256+int(0.5*text_height))

cv2.putText(img,text, 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)

#Display the image
cv2.imshow("img",img)

#Save image
cv2.imwrite("out.jpg", img)

cv2.waitKey(0)