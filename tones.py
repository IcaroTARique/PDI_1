import matplotlib.image as image
import matplotlib.pyplot as plt
from IPython.display import Image
import numpy as np

class Tones():
    def choiceTone(self,rgb):
        val = np.zeros(self.rgb.shape, dtype='uint8')
        val[:,:,rgb] = self.rgb[:,:,rgb]
        return val

    def RGBtone(self):
        rgb_tone = np.zeros(self.rgb.shape, dtype='uint8')
        print("RGBtone = ",rgb_tone)
        rgb_tone[:,:,0],rgb_tone[:,:,1],rgb_tone[:,:,2] = self.rgb[:,:,0],self.rgb[:,:,1],self.rgb[:,:,1]
        return rgb_tone

    def showTones(self, tone):
        print(tone)
        plt.imshow(tone)
        plt.show()