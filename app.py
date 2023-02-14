from PIL import ImageGrab
import time

def takeSS():
          image  = ImageGrab.grab()
          timeFormat = int(time.time())
          imageName = f"IMG_{timeFormat}.png"
          image.save(imageName)
          image.show()
          
if __name__ == "__main__":
          print("Taking ScreenShot in 3 seconds...")
          time.sleep(3)
          takeSS()
          