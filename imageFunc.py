import cv2
import numpy as np
from PIL import Image, ImageStat
import math

class ImageClass:
    def __init__(self, filedir, filename, image, size, hsvImage = []):
      self.filedir = filedir
      self.filename = filename
      self.image = image
      self.size = size
      self.hsvImage = hsvImage

      self.maxH = 0
      self.minH = 0
      self.sumH = 0
      self.averageH = 0

      self.maxS = 0
      self.minS = 0
      self.sumS = 0
      self.averageS = 0

      self.maxV = 0
      self.minV = 0
      self.sumV = 0
      self.averageV = 0

      self.maxR = 0
      self.minR = 0
      self.sumR = 0
      self.averageR = 0

      self.maxG = 0
      self.minG = 0
      self.sumG = 0
      self.averageG = 0

      self.maxB = 0
      self.minB = 0
      self.sumB = 0
      self.averageB = 0

      self.lfromLAB = 0
      self.luminance = 0
      self.way1 = 0
      self.way2 = 0
      self.way3 = 0
      self.way4 = 0
      self.way5 = 0

    def setHsvImage(self):
      self.hsvImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
      
    def calLFromLAB(self, dim=10, thresh=0.5):
      # Resize image to 10x10
      image = cv2.resize(self.image, (dim, dim))
      
      # Convert color space to LAB format and extract L channel
      L, A, B = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2LAB))
      
      # Normalize L channel by dividing all pixel values with maximum pixel value
      L = L/np.max(L)
      
      # If mean L greater than thresh is Brigth else Dark
      self.lfromLAB = np.mean(L)
      
    def calLuminance(self):
      # darkValue = 0
      luminance = 0
      for i in self.image:
        for j in i:
          r = j[2]
          g = j[1]
          b = j[0]
          luminance += (0.299 * ( r**2 ) + 0.587 * ( g**2 ) + 0.114 * ( b**2 ))
          # if luminance < 150:
          #   darkValue += 1
          
        
          
      self.luminance = luminance / (self.size * self.size)
      
    def calWay1(self):
      im = Image.open(self.filedir).convert('L')
      stat = ImageStat.Stat(im)
      self.way1 = stat.mean[0]
      
    def calWay2(self):
      im = Image.open(self.filedir).convert('L')
      stat = ImageStat.Stat(im)
      self.way2 = stat.rms[0]
      
    def calWay3(self):
      im = Image.open(self.filedir)
      stat = ImageStat.Stat(im)
      r,g,b = stat.mean
      self.way3 = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
      
    def calWay4(self):
      im = Image.open(self.filedir)
      stat = ImageStat.Stat(im)
      r,g,b = stat.rms
      self.way4 = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
      
    def calWay5(self):
      im = Image.open(self.filedir)
      stat = ImageStat.Stat(im)
      gs = (math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)) 
            for r,g,b in im.getdata())
      self.way5 = sum(gs)/stat.count[0]

    def setHsv(self):
      for i in self.hsvImage:
        for j in i:
          h = j[0]
          if h > self.maxH:
            self.maxH = h
          
          if h < self.minH:
            self.minH = h

          self.sumH += h

          s = j[1]
          if s > self.maxS:
            self.maxS = s
          
          if s < self.minS:
            self.minS = s

          self.sumS += s

          v = j[2]
          if v > self.maxV:
            self.maxV = v
          
          if v < self.minV:
            self.minV = v

          self.sumV += v

      self.averageH = self.sumH / (self.size * self.size)
      self.averageS = self.sumS / (self.size * self.size)
      self.averageV = self.sumV / (self.size * self.size)

    def setRgb(self):
      for i in self.image:
        for j in i:
          r = j[2]
          if r > self.maxR:
            self.maxR = r
          
          if r < self.minR:
            self.minR = r

          self.sumR += r

          g = j[1]
          if g > self.maxG:
            self.maxG = g
          
          if g < self.minG:
            self.minG = g

          self.sumG += g

          b = j[0]
          if b > self.maxB:
            self.maxB = b
          
          if b < self.minB:
            self.minB = b

          self.sumB += b

      self.averageR = self.sumR / (self.size * self.size)
      self.averageG = self.sumG / (self.size * self.size)
      self.averageB = self.sumB / (self.size * self.size)
      
    def getRow(self, count, filename, imageStatus):
      return [ count, filename, imageStatus, self.minH, self.maxH, self.sumH, round(self.averageH, 2),
                                            self.minS, self.maxS, self.sumS, round(self.averageS, 2),
                                            self.minV, self.maxV, self.sumV, round(self.averageV, 2),
                                            round(self.lfromLAB, 2), round(self.luminance, 2), round(self.way1, 2), 
                                            round(self.way2, 2), round(self.way3, 2), round(self.way4, 2), round(self.way5, 2),
                                            self.minR, self.maxR, self.sumR, round(self.averageR, 2),
                                            self.minG, self.maxG, self.sumG, round(self.averageG, 2),
                                            self.minB, self.maxB, self.sumB, round(self.averageB, 2) ]

      
    def reScaleV(self, arangeV, extraV):
      # self.hsvImage[:,:,2] += arangeV
          
      for idxi, i in enumerate(self.hsvImage):
        for indexj, j in enumerate(i):     
          v = j[2]
          count = v + extraV
          if count > 255:
            continue
            
          if count < 0:
            continue
          
          self.hsvImage[idxi][indexj][2] += extraV
