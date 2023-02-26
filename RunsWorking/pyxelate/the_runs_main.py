from skimage import io
from pyxelate import Pyx, Pal
# program to capture single image from webcam in python
  
# importing OpenCV library
import cv2 as cv
  
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam_port = 0
cam = cv.VideoCapture(cam_port)
  
# reading the input using the camera
result, image = cam.read()
  
# If image will detected without any error, 
# show result
if result:
  
    # showing result, it take frame name and image 
    # output
    cv.imshow("GeeksForGeeks", image)
    print("We made it")
    # saving image in local storage
    cv.imwrite("GeeksForGeeks.png", image)
    # If keyboard interrupt occurs, destroy image 
    # window
    cv.waitKey(0)
  
# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")

image = io.imread(r"C:\Users\apula\Desktop\RunsWorking\PicTesting\WIN_20230224_22_25_50_Pro.jpg")  

downsample_by = 14  # new image will be 1/14th of the original in size
palette = 7  # find 7 colors

# 1) Instantiate Pyx transformer
pyx = Pyx(factor=downsample_by, palette=palette)

# 2) fit an image, allow Pyxelate to learn the color palette
pyx.fit(image)

# 3) transform image to pixel art using the learned color palette
new_image = pyx.transform(image)

# save new image with 'skimage.io.imsave()'
io.imsave("pixel.png", new_image)