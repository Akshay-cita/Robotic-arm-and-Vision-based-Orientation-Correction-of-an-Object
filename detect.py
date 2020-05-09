from utils import *
from matplotlib import pyplot as plt
import subprocess
#from gtts import gTTS
import serial
import time

valueUp = "0"
valueDown = "180"

#GPIO.setmode(GPIO.BCM)

cam = cv2.VideoCapture(1)
s, test_img = cam.read()

ser = serial.Serial('COM7',115200,timeout=5) #Serial connection with arduino
ser.flush()
if ser.is_open:
     time.sleep(.5)
     print("COM7")
     time.sleep(.5)



max_val = 8
max_pt = -1
max_kp = 0

orb = cv2.ORB_create()
# orb is an alternative to SIFT

#test_img = read_img('files/tespython3 detect.pyt_100_2.jpg')
#test_img = read_img('files/test_50_2.jpg')
#test_img = read_img('files/test_20_2.jpg')
#test_img = read_img('files/pentagon3.jpg')
#test_img = read_img('files/test_20_4.jpg')

# resizing must be dynamic
original = test_img[200:700, 200:440]
display('original', original)

# keypoints and descriptors
# (kp1, des1) = orb.detectAndCompute(test_img, None)
(kp1, des1) = orb.detectAndCompute(original, None)

training_set = ['files/Up0.jpg','files/Up1.jpg','files/Up2.jpg','files/Down0.jpg','files/Down1.jpg','files/Down2.jpg'] #importig data set images
for i in range(0, len(training_set)):
	# train image
	train_img = cv2.imread(training_set[i])

	(kp2, des2) = orb.detectAndCompute(train_img, None)

	# brute force matcher
	bf = cv2.BFMatcher(cv2.NORM_L1,crossCheck=False)
	all_matches = bf.knnMatch(des1, des2, k=2)

	good = []
	# give an arbitrary number -> 0.789
	# if good -> append to list of good matches
	for (m, n) in all_matches:
		if m.distance < 0.9 * n.distance:
			good.append([m])

	if len(good) > max_val:
		max_val = len(good)
		max_pt = i
		max_kp = kp2

	print(i, ' ', training_set[i], ' ', len(good))

if max_val != 8:
	print(training_set[max_pt])
	print('good matches ', max_val)

	train_img = cv2.imread(training_set[max_pt])
	img3 = cv2.drawMatchesKnn(original, kp1, train_img, max_kp, good, 4)
	
	Rotation = str(training_set[max_pt])[6:-4]
	print('\nDetected Rotation is: ', Rotation)
	
	if Rotation.startswith("U",0,2) == True:
		print("Its Up")
		ser.write(valueUp.encode('UTF-8'))
		
	elif Rotation.startswith("D",0,2) == True:
		print("Its Down")
		ser.write(valueDown.encode('UTF-8'))
	(plt.imshow(img3), plt.show())
	
else:
	print('No Matches')
