# under Gnu Licsense ,please if you use it Refere to : 
# author :  amr abd el latief     
#author email : amrabdellatief1@gmail.com



#use :

#this Class is part of a program made in my Master Research in the field of Video Analysis 
# i made it apart of the other code ,because its useful
#you could use it for your operations on images if you need it 

#liscense:

# This Class is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This Class is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this Class.  If not, see <http://www.gnu.org/licenses/>.




from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp
import operator
import math
import random
import cv2
import numpy as np

class Terminals:
        
        #########################For wiriting on images

        def wimage(self,img,listOfValues):
                img2 = img[:]
                for l in listOfValues:
                   #print l     
                   img2[l][0]=0
                   img2[l][1]=0
                   img2[l][2]=255
                return img2
                        

        #########################Image Processing Functions  for the IRO Stage ######################################################
        #remove elements of list

		# get dx of image 
        def dx(self,img):
                o =np.uint8(img)    
                imgx = cv2.Sobel(o,cv2.CV_8U,1,0,ksize=5)
                return np.uint8(imgx)


        def dxx(self,img):
                o = np.uint8(img)
                imgx = cv2.Sobel(o,cv2.CV_16U,1,0,ksize=5)
                imgxx=cv2.Sobel(imgx,cv2.CV_16U,1,0,ksize=5)
                return np.uint8(imgxx)

        def dy(self,img):
                o = np.uint8(img)
                imgy = cv2.Sobel(o,cv2.CV_16U,0,1,ksize=5)
                return np.uint8(imgy)


        def dyy(self,img):
                o = np.uint8(img)
                imgy = cv2.Sobel(o,cv2.CV_16U,0,1,ksize=5)
                imgyy = cv2.Sobel(imgy,cv2.CV_16U,0,1,ksize=5)
                return np.uint8(imgyy)

        def dxy(self,img):
                o = np.uint8(img)
                imgx = cv2.Sobel(o,cv2.CV_16U,1,0,ksize=5)
                imgxy = cv2.Sobel(imgx,cv2.CV_16U,0,1,ksize=5)
                return np.uint8(imgxy)
        # define fine for square an image -> image

        def power(self,l):
                #t = np.array(l)
                #t=l
                h = np.uint8(np.multiply(np.uint32(l),np.uint32(l)))
                return h

        # define Gaussian Function for sigma = 1 

        def Gausssigma1(self,img):
                temp8 =np.uint8(img)
                blur = cv2.GaussianBlur(temp8,(5,5),1)
                return np.uint8(blur)

        # define Gaussian Function for sigma = 2

        def Gausssigma2(self,img):
                
                temp8 =np.absolute(np.uint8(img))
                blur = cv2.GaussianBlur(temp8,(5,5),2)
                return np.uint8(blur)


        # define a 0.05 function

        def halffunc(self,input):
         return np.uint8(0.05*np.uint32(input))



        def listRemove(self,listparam):
                for i in range (0,len(listparam)):
                        listparam.pop()

          

        # function to extract the Blue Component of image



        def log(self,image):
          i = image
          j=i
          for k in range(0,len(image)-1):  
              for l in range(0,len(image[0])-1):
                  j[k][l][0]=log(i[k][l][0])
                  j[k][l][1]=log(i[k][l][1])
                  j[k][l][2]=log(i[k][l][2])
                  
          return np.uint8(j)


        ############# Color Conversion Functions  image -> image


        # RGB to HSV Section V means I

        print "----------------------------"

        def h(self,image):
             i = image
             print "1"
             j=i
             print "2"
             hsv = cv2.cvtColor(j, cv2.COLOR_BGR2HSV)
             
             print "4"
             print "5"
             for k in range(0,len(image)):  #to iterate between 10 to 20
                for l in range(0,len(image[0])):
                   hsv[k][l][1]=0
                   hsv[k][l][2]=0
             return np.uint8(j)
        def s(self,img):
             hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
             i = hsv
             j=i
             for k in range(0,len(image)):  #to iterate between 10 to 20
                for l in range(0,len(image[0])):
                   j[k][l][0]=0
                   j[k][l][2]=0
             return np.uint8(j)

        def v(self,img):
             hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
             i = hsv
             j=i
             for k in range(0,len(image)):  #to iterate between 10 to 20
                for l in range(0,len(image[0])):
                   j[k][l][0]=0
                   j[k][l][1]=0
             return np.uint8(j)
          

        # function to extract the Blue Component of image

        def b(self,image):
          i = image[:]
          j=i[:]
          for k in range(0,len(image)):  #to iterate between 10 to 20
              for l in range(0,len(image[0])):
                  j[k][l][1]=0
                  j[k][l][2]=0
                  
          return np.uint8(j)


        # function to extract the Green Component of image

        def g(self,image):
          i = image[:]
          j=i[:]
          for k in range(0,len(image)):  #to iterate between 10 to 20
              for l in range(0,len(image[0])):
                  j[k][l][0]=0
                  j[k][l][2]=0
          return np.uint8(j)

        # function to extract the Red Component of image

        def r(self,image):
          i = image[:]
          j=i[:]
          for k in range(0,len(image)):  #to iterate between 10 to 20
              for l in range(0,len(image[0])):
                  j[k][l][0]=0
                  j[k][l][1]=0
          return np.uint8(j)

        ###############CMYK -> image (c,0,0) , (m,0,) 

        ######################################################################################

        # operation functions 


        # floating point operators

        def sqrtfun(self,img):
                return np.uint32(np.sqrt(np.uint32(img)))

        # Define a safe division function
        def safeDiv(self,left, right):
            try: return np.uint32(np.divide(np.uint32(left),np.uint32(right)))
            except ZeroDivisionError: return 0


        def absoluteadd(self,left,right):
                return np.absolute(np.add(np.uint32(left),np.uint32(right)))
                
        def absolutesub(self,left,right):
                return np.absolute(np.subtract(np.uint32(left),np.uint32(right)))


