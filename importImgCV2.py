import cv2

birjon = cv2.imread('pixel-3.jpg')
birjon[10:50, 100:110] = (0,0,255)
cv2.imshow('image', birjon)
cv2.waitKey(0)
cv2.destroyAllWindows()