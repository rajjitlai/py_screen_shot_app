# COPYRIGHT INFO
'''
AUTHOR: RAJJIT LAISHRAM
DATE CREATED: 14-02-2023
PURPOSE: A SMALL SCREENSHOT APPLICATION TO TAKE SS ANYTIME
'''

from PIL import ImageGrab  # pip install PILLOW
import time

def takeSS():  # function definition
          image  = ImageGrab.grab()  # to capture the image
          timeFormat = int(time.time())  # filename with the time
          imageName = f"IMG_{timeFormat}.png"  #filename with png extension
          image.save(imageName)  # saving the image
          image.show()  # to preview the captured  image with the default image viewer
          
if __name__ == "__main__":  # main part of the program
          print("Taking ScreenShot in 3 seconds...")  # 3 seconds timer notice
          time.sleep(3)   # timer
          takeSS()  # calling the function
          