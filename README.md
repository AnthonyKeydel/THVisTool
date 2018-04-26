# THVisTool
Quick python tool to help visualize how the different parameters of thresholding affect the end result.

Press any key to switch between Settings and Image. (PLEASE CHECK BUG SECTION)

# Settings
Blur - changes the amount the image is blurred by.

Adapt - enable or disable adaptive thresholding
  • 0 is normal thresholding
  • 1 is adaptive thresholding
    ○ Adaptive thresholding only works with a TH_Type of 0 or 1

TH_Type - Changes the type of thresholding
	• 0: Binary
	• 1: Binary Inverted
	• 2: Threshold Truncated
	• 3: Threshold to Zero
	• 4: Threshold to Zero Inverted

NonAdaptVal - Changes the thresh value in non-adaptive thresholding

AdaptBlockSize - Changes the block size for adaptive thresholding
AdaptConst - Changes the constant value for adaptive thresholding
 
To exit, change the EXIT setting to 0, and press any key 3 times. (explained more in the bug below)

# KNOWN BUGS:
The changes don't show up the first time you switch to the image tab, you have to press a key 3 times to go to the image, back to settings, then to the updated image.
