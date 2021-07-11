import cv2

class SummaryImage:
    def __init__(self):
      self.minAverageR = 300
      self.minAverageG = 300
      self.minAverageB = 300
      self.minAverageH = 300
      self.minAverageS = 300
      self.minAverageV = 300
      
      self.minAverageRImage = ''
      self.minAverageGImage = ''
      self.minAverageBImage = ''
      self.minAverageHImage = ''
      self.minAverageSImage = ''
      self.minAverageVImage = ''

      self.maxAverageR = 0
      self.maxAverageG = 0
      self.maxAverageB = 0
      self.maxAverageH = 0
      self.maxAverageS = 0
      self.maxAverageV = 0
      
      self.maxAverageRImage = ''
      self.maxAverageGImage = ''
      self.maxAverageBImage = ''
      self.maxAverageHImage = ''
      self.maxAverageSImage = ''
      self.maxAverageVImage = ''
      
      self.avAverageR = 0
      self.avAverageG = 0
      self.avAverageB = 0
      self.avAverageH = 0
      self.avAverageS = 0
      self.avAverageV = 0
    
    def summary(self, imageClass, filename):
      # R
      if imageClass.averageR < self.minAverageR:
        self.minAverageR = imageClass.averageR
        self.minAverageRImage = filename
      
      if imageClass.averageR > self.maxAverageR:
        self.maxAverageR = imageClass.averageR
        self.maxAverageRImage = filename

      self.avAverageR += imageClass.averageR
      
      # G
      if imageClass.averageG < self.minAverageG:
        self.minAverageG = imageClass.averageG
        self.minAverageGImage = filename
      
      if imageClass.averageG > self.maxAverageG:
        self.maxAverageG = imageClass.averageG
        self.maxAverageGImage = filename

      self.avAverageG += imageClass.averageG
      
      # B
      if imageClass.averageB < self.minAverageB:
        self.minAverageB = imageClass.averageB
        self.minAverageBImage = filename
      
      if imageClass.averageB > self.maxAverageB:
        self.maxAverageB = imageClass.averageB
        self.maxAverageBImage = filename

      self.avAverageB += imageClass.averageB
      
      # H
      if imageClass.averageH < self.minAverageH:
        self.minAverageH = imageClass.averageH
        self.minAverageHImage = filename
      
      if imageClass.averageH > self.maxAverageH:
        self.maxAverageH = imageClass.averageH
        self.maxAverageHImage = filename

      self.avAverageH += imageClass.averageH
      
      # S
      if imageClass.averageS < self.minAverageS:
        self.minAverageS = imageClass.averageS
        self.minAverageSImage = filename
      
      if imageClass.averageS > self.maxAverageS:
        self.maxAverageS = imageClass.averageS
        self.maxAverageSImage = filename

      self.avAverageS += imageClass.averageS
      
      # V
      if imageClass.averageV < self.minAverageV:
        self.minAverageV = imageClass.averageV
        self.minAverageVImage = filename
      
      if imageClass.averageV > self.maxAverageV:
        self.maxAverageV = imageClass.averageV
        self.maxAverageVImage = filename

      self.avAverageV += imageClass.averageV

    def getRowArray(self, count):
      minAverageH = ['1', self.minAverageHImage, 'Min Average H', round(self.minAverageH, 2)]
      minAverageS = ['2', self.minAverageSImage, 'Min Average S', round(self.minAverageS, 2)]
      minAverageV = ['3', self.minAverageVImage, 'Min Average V', round(self.minAverageV, 2)]
      minAverageR = ['4', self.minAverageRImage, 'Min Average R', round(self.minAverageR, 2)]
      minAverageG = ['5', self.minAverageGImage, 'Min Average G', round(self.minAverageG, 2)]
      minAverageB = ['6', self.minAverageBImage, 'Min Average B', round(self.minAverageB, 2)]
      
      maxAverageH = ['7', self.maxAverageHImage, 'Max Average H', round(self.maxAverageH, 2)]
      maxAverageS = ['8', self.maxAverageSImage, 'Max Average S', round(self.maxAverageS, 2)]
      maxAverageV = ['9', self.maxAverageVImage, 'Max Average V', round(self.maxAverageV, 2)]
      maxAverageR = ['10', self.maxAverageRImage, 'Max Average R', round(self.maxAverageR, 2)]
      maxAverageG = ['11', self.maxAverageGImage, 'Max Average G', round(self.maxAverageG, 2)]
      maxAverageB = ['12', self.maxAverageBImage, 'Max Average B', round(self.maxAverageB, 2)]
      
      avAverageH = ['13', '', 'Average Average H', round(self.avAverageH / count, 2)]
      avAverageS = ['14', '', 'Average Average S', round(self.avAverageS / count, 2)]
      avAverageV = ['15', '', 'Average Average V', round(self.avAverageV / count, 2)]
      avAverageR = ['16', '', 'Average Average R', round(self.avAverageR / count, 2)]
      avAverageG = ['17', '', 'Average Average G', round(self.avAverageG / count, 2)]
      avAverageB = ['18', '', 'Average Average B', round(self.avAverageB / count, 2)]
      
      return [minAverageH, minAverageS, minAverageV, minAverageR, minAverageG, minAverageB, 
              maxAverageH, maxAverageS, maxAverageV, maxAverageR, maxAverageG, maxAverageB,
              avAverageH, avAverageS, avAverageV, avAverageR, avAverageG, avAverageB ]
      
    