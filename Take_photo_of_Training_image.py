import cv2
import time

cam = cv2.VideoCapture(1)


for i in range(3):
	s, img_before = cam.read()
	crop = img_before[200:700, 200:440]
	#time.sleep(2)
	cv2.imshow("Test Picture", crop) 
	cv2.waitKey(1)
	cv2.imwrite("files/Down"+str(i)+".jpg",crop) 
	cv2.waitKey(0)
	#img = cv2.imread('test.jpg', 1)
	#print(img.shape)
	 	 
	
cv2.waitKey(0)
cv2.destroyAllWindows()





