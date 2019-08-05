import matplotlib.image as image
import matplotlib.pyplot as plt
from IPython.display import Image
import numpy as np

class Tones():
    def Rtone(self):
        red = np.zeros(self.rgb.shape, dtype='uint8')
        red[:,:,0] = self.rgb[:,:,0]
        return red
    
    def Gtone(self):
        green = np.zeros(self.rgb.shape, dtype='uint8')
        green[:,:,1] = self.rgb[:,:,1]
        return green

    def Btone(self):
        blue = np.zeros(self.rgb.shape, dtype='uint8')
        blue[:,:,2] = self.rgb[:,:,2]
        return blue

    def RGBtone(self):
        rgb_tone = np.zeros(self.rgb.shape, dtype='uint8')
        print("RGBtone = ",rgb_tone)
        rgb_tone[:,:,0],rgb_tone[:,:,1],rgb_tone[:,:,2] = self.rgb[:,:,0],self.rgb[:,:,1],self.rgb[:,:,1]
        return rgb_tone

    def showTones(self, tone):
        print(tone)
        plt.imshow(tone)
        plt.show()