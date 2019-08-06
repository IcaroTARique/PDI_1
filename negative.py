import matplotlib.image as image
import matplotlib.pyplot as plt
from IPython.display import Image
import numpy as np

class Negative():
    def choiceNegTone(self,rgb):
        val = np.zeros(self.rgb.shape, dtype='uint8')
        val[:,:,rgb] = (255 - self.rgb[:,:,rgb])
        return val

    def RGBNtone(self):
        rgb_tone = np.zeros(self.rgb.shape, dtype='uint8')
        rgb_tone[:,:,0],rgb_tone[:,:,1],rgb_tone[:,:,2] = (255 - self.rgb[:,:,0]),(255 - self.rgb[:,:,1]),( 255 - self.rgb[:,:,1])
        return rgb_tone
    
class NegativeUnchanged():
    def choiceNegUnchTone(self,rgb):
        val = np.copy(self.rgb)
        val[:,:,rgb] = (255 - self.rgb[:,:,rgb])
        return val

class NegativeYiq():
    def YNtone(self):
        yiq = np.copy(self.yiq)
        yiq[:,:,0] = (255 - self.yiq[:,:,0])
        print(yiq)
        return yiq