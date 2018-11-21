import cv2
import math
import numpy as np

class rotator:

    angle = 20.0
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

    def rotate(self):
        emptyF = np.zeros((self.width,self.height),dtype="uint8")
        emptyB = np.zeros((self.width,self.height),dtype="uint8")
        emptyBB = np.zeros((self.width,self.height),dtype="uint8")


        for i in range(self.width):
            for j in range(self.height):


                temp = self.img[i,j]

                ix = i-self.x
            #    cosX = int(ix*math.cos(self.radians))
            #    sinX = int(ix*math.sin(self.radians))


                jy = j-self.y
            #    sinY = int(jy*math.sin(self.radians))
            #    cosY = int(jy*math.cos(self.radians))

                #forward mapping
                #xf = (cosX-sinY)+self.x
                #yf = (sinX+cosY)+self.x

                xf = int((i-self.x)*math.cos(self.radians)-(j-self.y)*math.sin(self.radians))+self.x
                yf = int((i-self.x)*math.sin(self.radians)+(j-self.y)*math.cos(self.radians))+self.x


                #backward map of the forward mapped picture
                xb = (xf-self.x)*math.cos(self.radians)+(yf-self.y)*math.sin(self.radians)+self.x
                yb = -(xf-self.x)*math.sin(self.radians)+(yf-self.y)*math.cos(self.radians)+self.x


                #backward map of the original image
                xbb = int((i-self.x)*math.cos(self.radians)+(j-self.y)*math.sin(self.radians)+self.x)
                ybb = int(-(i-self.x)*math.sin(self.radians)+(j-self.y)*math.cos(self.radians)+self.x)


            #    xbb = cosX+sinY+self.x
            #    ybb = -sinX+cosY+self.x


                if xf < 660 and yf < 660 and xf>0 and yf > 0:
                    emptyF[int(xf),int(yf)] = temp
                else:
                    pass

                if xb < 660 and yb < 660 and xb>0 and yb > 0:
                    emptyB[int(xb),int(yb)] = temp
                else:
                    pass

                if xbb < 660 and ybb < 660 and xbb>0 and ybb > 0:
                    emptyBB[(xbb),(ybb)] = temp
                else:
                    pass

        cv2.imshow('Forward', emptyF)
        cv2.imshow('Forward Backward', emptyB)
        cv2.imshow('Backward', emptyBB)

def main():
    rotator.showImg('normal', rotator)
    rotator.printWH(rotator)
    rotator.rotate(rotator)
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__ == '__main__':
    main()
