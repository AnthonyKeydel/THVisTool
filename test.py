# Standard imports
import cv2
import numpy as np;
 
# Read image
img = cv2.imread("4.png", cv2.IMREAD_GRAYSCALE)

blur = cv2.GaussianBlur(img,(11,11),0)


ret, imgTHB = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
imgTHA = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15,5) 
# Show other image
cv2.imshow("", imgTHA)
cv2.waitKey(0)


params = cv2.SimpleBlobDetector_Params()

#params.minThreshold = 2;
#params.maxThreshold = 50;
#
params.filterByArea = True
params.minArea = 100
# params.filterByCircularity = True
# params.minCircularity = .95

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)
 
# Detect blobs.
keypoints = detector.detect(imgTHA)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", img_with_keypoints)
cv2.waitKey(0)