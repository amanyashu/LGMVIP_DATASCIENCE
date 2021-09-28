import cv2
image=cv2.imread("girl.jpg")
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted_image=cv2.bitwise_not(grey_image)
blur_image=cv2.GaussianBlur(inverted_image,(21,21),00)
inverted_blur_image=cv2.bitwise_not(blur_image)
sktech=cv2.divide(grey_image,inverted_blur_image,scale=256.0)
cv2.imwrite("sktech.png",sktech)