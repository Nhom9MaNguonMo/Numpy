import cv2
import numpy as np
img=cv2.imread("hocmay\VYBH3049.PNG")
rows, cols =img.shape[:2]
kernel_identity= np.array([[0,0,0],[0,1,0],[0,0,0]])
kernel_3x3=np.ones((3,3),np.float32)
kernel_5x5=np.ones((5,5),np.float32)
cv2.imshow('Original',img)
output= cv2.filter2D(img,-1,kernel_identity)
cv2.imshow("Identity filter",output)
output= cv2.filter2D(img,-5,kernel_3x3)
cv2.imshow("3x3 filter",output)
print(rows,cols)
output = cv2.filter2D(img[0:100,0:100], -1, kernel_5x5)
for i in range(1,100):
    for j in range(1,100):
        img[i,j]=output[i,j]
cv2.imshow('5x5 filter',img)
cv2.waitKey(0)