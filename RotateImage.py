import cv2
import math
import numpy as np

class rotator:

    angle = 30.0
    x = 330
    y = 330

    radians = float(angle*(math.pi/180))
    img = cv2.imread('lena.jpg',0)
    width,height = img.shape

    def showImg(name, self):
        cv2.imshow(name, self.img)
        self.img = np.pad(self.img, (self.height) ,'constant', constant_values=0)
        self.width,self.height = self.img.shape

    def printWH(self):
        print(self.width)
        print(self.height)

    def getImage(self):
        return self.img

    #Rotates an image using forward mapping
    def forward(self, img):
        empty = np.zeros((self.width,self.height),dtype="uint8")

        for i in range(self.width):
            for j in range(self.height):

                #forward mapping
                x = int((i-self.x)*math.cos(self.radians)-(j-self.y)*math.sin(self.radians))+self.x
                y = int((i-self.x)*math.sin(self.radians)+(j-self.y)*math.cos(self.radians))+self.x

                if x < self.width and y < self.height and x>0 and y > 0:
                    empty[i,j] = self.img[int(x),int(y)]
                else:
                    pass

        return empty

    #Rotates an image using backward mapping
    def backward(self, img):
        empty = np.zeros((self.width,self.height),dtype="uint8")

        for i in range(self.width):
            for j in range(self.height):

                #forward mapping
                x = int((i-self.x)*math.cos(self.radians)+(j-self.y)*math.sin(self.radians))+self.x
                y = int(-(i-self.x)*math.sin(self.radians)+(j-self.y)*math.cos(self.radians))+self.x

                if x < self.width and y < self.height and x>0 and y > 0:
                    empty[i,j] = self.img[int(x),int(y)]
                else:
                    pass

        return empty

    #Rotates an image using forward mapping and then rotates it back using backward mapping
    def backwardForward(self, img):
        empty = np.zeros((self.width,self.height),dtype="uint8")

        for i in range(self.width):
            for j in range(self.height):

                #forward mapping
                xO = int((i-self.x)*math.cos(self.radians)-(j-self.y)*math.sin(self.radians))+self.x
                yO = int((i-self.x)*math.sin(self.radians)+(j-self.y)*math.cos(self.radians))+self.x

                x = int((xO-self.x)*math.cos(self.radians)+(yO-self.y)*math.sin(self.radians))+self.x
                y = int(-(xO-self.x)*math.sin(self.radians)+(yO-self.y)*math.cos(self.radians))+self.x

                if x < self.width and y < self.height and x>0 and y > 0:
                    empty[i,j] = self.img[int(x),int(y)]
                else:
                    pass

        return empty

def main():
    rotator.showImg('normal', rotator)
    rotator.printWH(rotator)
    cv2.imshow('forward', rotator.forward(rotator, rotator.getImage(rotator)))
    cv2.imshow('backward', rotator.backward(rotator, rotator.getImage(rotator)))
    cv2.imshow('foward image backward', rotator.backwardForward(rotator, rotator.getImage(rotator)))
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__ == '__main__':
    main()
