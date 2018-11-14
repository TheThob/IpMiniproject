import cv2
import math
import numpy as np

class rotator:

    height = 0
    width = 0
    angle = 45
    radians = angle*(math.pi/180)
    img = cv2.imread('lena.jpg',0)


    #def __init__(self):
    #    pass

    def showImg(name, self):

        cv2.imshow(name, self.img)
        self.width,self.height = self.img.shape
        self.img = np.pad(self.img, (220) ,'constant', constant_values=0)

    def printWH(self):
        print(self.width)
        print(self.height)

    def rotate(self):
        emptyF = np.zeros((self.width,self.height),dtype="uint8")
        emptyB = np.zeros((self.width,self.height),dtype="uint8")


        for x in range(self.width):
            for y in range(self.height):


                #alpha = 1 * math.cos(self.radians)
                #beta = 1 * math.sin(self.radians)
                temp = self.img[x,y]

                #forward mapping
                xf = (x-self.width/2)*math.cos(self.radians)-(y-self.height/2)*math.sin(self.radians)+self.width/2
                yf = (x-self.width/2)*math.sin(self.radians)+(y-self.height/2)*math.cos(self.radians)+self.width/2

                #backward mapping
                xb = (x-self.width/2)*math.cos(self.radians)+(y-self.height/2)*math.sin(self.radians)+self.width/2
                yb = -(x-self.width/2)*math.sin(self.radians)+(y-self.height/2)*math.cos(self.radians)+self.width/2

                if xb < 660 and yb < 660 and xb>0 and yb > 0:
                    emptyF[int(xf),int(yf)] = temp





        cv2.imshow('Forward', emptyF)

def main():
    rotator.showImg('normal', rotator)
    rotator.printWH(rotator)
    rotator.rotate(rotator)
    #rotator.showImg('rotated', rotator)
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__ == '__main__':
    main()
