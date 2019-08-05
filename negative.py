import matplotlib.image as image
import matplotlib.pyplot as plt
from IPython.display import Image
import numpy as np

class Negative():
    #SINGLE CHANEL
    def RNtone(self):
        red = np.zeros(self.rgb.shape, dtype='uint8')
        red[:,:,0] = (255 - self.rgb[:,:,0])
        return red
    
    def GNtone(self):
        green = np.zeros(self.rgb.shape, dtype='uint8')
        green[:,:,1] = (255 - self.rgb[:,:,1])
        return green

    def BNtone(self):
        blue = np.zeros(self.rgb.shape, dtype='uint8')
        blue[:,:,2] = (255 - self.rgb[:,:,2])
        return blue

    def RGBNtone(self):
        rgb_tone = np.zeros(self.rgb.shape, dtype='uint8')
        rgb_tone[:,:,0],rgb_tone[:,:,1],rgb_tone[:,:,2] = (255 - self.rgb[:,:,0]),(255 - self.rgb[:,:,1]),( 255 - self.rgb[:,:,1])
        return rgb_tone
    
class NegativeUnchanged():
    def RNUtone(self):
        # red = np.zeros(self.rgb.shape, dtype='uint8')
        # red[:,:,:] = self.rgb[:,:,:]
        red = np.copy(self.rgb)
        red[:,:,0] = (255 - self.rgb[:,:,0])
        return red

    def GNUtone(self):
        # green = np.zeros(self.rgb.shape, dtype='uint8')
        # green[:,:,:] = self.rgb[:,:,:]
        green = np.copy(self.rgb)
        green.setflags(write=1)
        green[:,:,1] = (255 - self.rgb[:,:,1])
        return green

    def BNUtone(self):
        # blue = np.zeros(self.rgb.shape, dtype='uint8')
        # blue[:,:,:] = self.rgb[:,:,:]
        blue = np.copy(self.rgb)
        blue.setflags(write=1)
        blue[:,:,2] = (255 - self.rgb[:,:,2])
        return blue

class NegativeYiq():
    def YNtone(self):
        yiq = np.copy(self.yiq)
        yiq[:,:,0] = (255 - self.yiq[:,:,0])
        print(yiq)
        return yiq