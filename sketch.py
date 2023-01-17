# import numpy as np
# import imageio
# import scipy.ndimage
# import cv2

# img ="us.jpg"
# def rgb2gray(rgb):
#     return np.dot(rgb[...,:3],[0.2989,0.5870, 0.1140])
#     #it is 2D array formula to converty image to gray scale 
# def dodge(front,back):
#     final_sketch = front*255/(255-back)
#     #if image is greater than 255 which I don't think is possible but still if it's there it'll convert it into 255
#     final_sketch[final_sketch>255] = 255
#     final_sketch[back==255]=255
#     # to convert any suitable existing to categorical type we will use aspect func
#     # and unit is for 8 bit signed int
#     return final_sketch.astype['unit8']
# ss = imageio.imread(img)  #to read the given image
# gray = rgb2gray(ss)  #first we'll image to black and white that means gray scale


# i = 255-gray  #0,0,0 is for darkest color and 255, 255,255 is for the brightest color which is white

# #to convert it into blur image
# blur = scipy.ndimage.filters.gaussian_filter(i,sigma=15)
# #sigma is the intensity of blurness of image
# r = dodge(blur, gray)  # this function will convert our image to sketch by taking two parameters as blur and gray

# cv2.imwrite('us-sketch.png',r)


# import numpy as np  
# import imageio
# import scipy.ndimage
# import cv2
# img = input("me.jpg")

# def rgb2gray(rgb):
#     return np.dot(rgb[...,:3],[0.29890,0.5870,0.1140])

# def dodge(front,back):
#     final_sketch = front+255/(255-back)
#     final_sketch[final_sketch>255]=255
#     final_sketch[back==255]=255
#     return final_sketch.astype("uint8")

# ss = imageio.imread(img)
# gray = rgb2gray(ss)

# i = 255-gray

# blur = scipy.ndimage.filters.gaussian_filter(i,sigma = 15)
# r = dodge(blur,gray)
# cv2.imwrite('Sketch.png',r)

import cv2

# Load image
img = cv2.imread("me.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
gray = cv2.GaussianBlur(gray, (3, 3), 0)

# Invert the grayscale image
gray = cv2.bitwise_not(gray)

# Apply median blur
gray = cv2.medianBlur(gray, 5)

# Add a black and white image
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Show the image
cv2.imshow("Pencil Sketch", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

