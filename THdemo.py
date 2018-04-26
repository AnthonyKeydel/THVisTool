# Standard imports
import cv2
import numpy as np;

def nothing(x):
    pass

# Read image
img = cv2.imread("1.png", cv2.IMREAD_GRAYSCALE)

# cv2.imshow("Original", img)
# cv2.waitKey(0)

cv2.namedWindow('settings')

cv2.createTrackbar('blur', 'settings', 13, 31, nothing)
	# 0-99 amount of blur --- must be odd, or the image will not blur

cv2.createTrackbar('adapt', 'settings', 0, 1, nothing)
	# 0: Not Adaptive 
	# 1: Adaptive --- only works with TH_Type = 0 or 1 

cv2.createTrackbar('TH_Type', 'settings', 0, 4, nothing)
	# 0: Binary
	# 1: Binary Inverted
	# 2: Threshold Truncated
	# 3: Threshold to Zero
	# 4: Threshold to Zero Inverted

cv2.createTrackbar('nonAdaptVal', 'settings', 100, 255, nothing)
	# For use with non-adaptive 

cv2.createTrackbar('adaptBlockSize', 'settings', 0, 50, nothing)
	# Adaptive block size --- must be odd, or will default to 3
cv2.createTrackbar('adaptConst', 'settings', 5, 10, nothing)
	# Constant subtracted from the mean (im not sure what it does...)
	# It can be positive OR negative, so im giving it a range(-5,5)
	#  by subtracting 5 from the input value

cv2.createTrackbar('EXIT', 'settings', 1, 1, nothing)
exitTB = 1

while(exitTB):
	blurTB = cv2.getTrackbarPos('blur','settings')
	if (blurTB%2==0):
		blurTB+=1
	adapTB = cv2.getTrackbarPos('adapt','settings')
	typeTB = cv2.getTrackbarPos('TH_Type','settings')
	nonAdaptValTB = cv2.getTrackbarPos('nonAdaptVal','settings')
	blockSizeTB = cv2.getTrackbarPos('adaptBlockSize','settings')
	if(blockSizeTB%2==0):
		blockSizeTB+=1
	if(blockSizeTB<2):
		blockSizeTB=3  
	constTB = cv2.getTrackbarPos('adaptConst','settings') -5
	exitTB = cv2.getTrackbarPos('EXIT', 'settings')


	if(typeTB==0):
		TH_Type = cv2.THRESH_BINARY 
	elif(typeTB==1):
		TH_Type = cv2.THRESH_BINARY_INV 
	elif(typeTB==2):
		TH_Type = cv2.THRESH_TRUNC
	elif(typeTB==3):
		TH_Type = cv2.THRESH_TOZERO 
	elif(typeTB==4):
		TH_Type = cv2.THRESH_TOZERO_INV

	if(blurTB%2==0):
		blurImg = img;
	else:
		blurImg = cv2.GaussianBlur(img,(blurTB,blurTB),0)

	# If thresholding is adaptive:
	if(adapTB and (TH_Type == cv2.THRESH_BINARY or TH_Type == cv2.THRESH_BINARY_INV)):
		imgTH = cv2.adaptiveThreshold(blurImg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		TH_Type, blockSizeTB, constTB)
	# If thresholding is NOT adaptive:
	else:
		ret, imgTH = cv2.threshold(blurImg,nonAdaptValTB,255,TH_Type) 

	cv2.waitKey(0)

	cv2.imshow('image', imgTH)

	cv2.waitKey(0)
	cv2.destroyWindow('image')

if(adapTB):
	print("Blur: ", blurTB, " TH_Type: ", TH_Type, " Value: ", nonAdaptValTB)
else:
	print("Blur: ", blurTB, " TH_Type: ", TH_Type, " Block Size: ", blockSizeTB, " Const: ", constTB)



cv2.destroyAllWindows()