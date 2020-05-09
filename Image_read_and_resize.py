import numpy as np
import cv2
import math
#from scipy import ndimage


cam = cv2.VideoCapture(1)

while True:
	
	s, img_before = cam.read()
	crop = img_before[200:700, 200:440] #heght x width
	
	cv2.imshow("Resized Image", crop)  
	cv2.waitKey(1)  
	
#key = cv2.waitKey(0)
cv2.waitKey()
cv2.destroyAllWindows()
