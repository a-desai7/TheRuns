from skimage import io
from pyxelate import Pyx, Pal
# program to capture single image from webcam in python
import cv2 as cv
import time 
import subprocess

# SET THE COUNTDOWN TIMER
# for simplicity we set it to 3
# We can also take this as input
TIMER = int(5)
   
# Open the camera
cap = cv.VideoCapture(0)
open = True
second = True

while True:
      
    # Read and display each frame
    ret, img = cap.read()
    cv.imshow('a', img)

    # check for the key pressed
    k = cv.waitKey(125)

    # set the key for the countdown
    # to begin. Here we set q
    # if key pressed is q
    if k == ord(' '):
        prev = time.time()
  
        while TIMER >= 0:
            ret, img = cap.read()
  
            # Display countdown on each frame
            # specify the font and draw the
            # countdown using puttext
            font = cv.FONT_HERSHEY_SIMPLEX
            cv.putText(img, str(TIMER), 
                        (200, 250), font,
                        7, (0, 255, 255),
                        4, cv.LINE_AA)
            cv.imshow('a', img)
            cv.waitKey(125)
  
            # current time
            cur = time.time()
  
            # Update and keep track of Countdown
            # if time elapsed is one second 
            # then decrease the counter
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
  
        else:
            ret, img = cap.read()
  
            # Display the clicked frame for 2 
            # sec.You can increase time in 
            # waitKey also
            cv.imshow('a', img)
  
            # time for which image displayed
            cv.waitKey(2000)
  
            # Save the frame
            cv.imwrite('camera.jpg', img)
            break
  
            # HERE we can reset the Countdown timer
            # if we want more Capture without closing
            # the camera
  
# close the camera
cap.release()
   
# close all the opened windows
cv.destroyAllWindows()

image = io.imread(r"camera.jpg")  

downsample_by = 4  # new image will be 1/14th of the original in size
palette = 15  # find 7 colors

# 1) Instantiate Pyx transformer
pyx = Pyx(factor=downsample_by, palette=palette)

# 2) fit an image, allow Pyxelate to learn the color palette
pyx.fit(image)

# 3) transform image to pixel art using the learned color palette
new_image = pyx.transform(image)

# save new image with 'skimage.io.imsave()'
io.imsave("pixel.png", new_image)

subprocess.run(['python', 'RunsWorking\pyxelate\DropImage.py'])