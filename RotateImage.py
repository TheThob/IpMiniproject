import cv2
import math

class rotator:

    height = 0
    width = 0
    angle = 90

    def __init__(self):
        pass

    def showImg(arg,name, self):
        img = cv2.imread(arg,0)
        cv2.imshow(name, img)
        self.width,self.height = img.shape
    def printWH(self):
        print(self.width)
        print(self.height)
    def rotate(self):
        for x in range(self.width):
            for y in range(self.height):
                x = x*math.cos(self.angle)-y*math.sin(self.angle)
                y = x*math.sin(self.angle)+y*math.cos(self.angle)

def main():
    rotator.showImg('lena.jpg','normal', rotator)
    rotator.printWH(rotator)
    rotator.rotate(rotator)
    rotator.showImg('lena.jpg','rotated', rotator)
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__ == '__main__':
    main()
