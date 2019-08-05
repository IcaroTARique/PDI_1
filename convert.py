import matplotlib.image as image
import matplotlib.pyplot as plt
from IPython.display import Image
import numpy as np

class Convert():

    def RGBtoYIQ(self): 
        for i in range(len(self.rgb)):
            for j in range(len(self.rgb[i])):
                self.yiq[i,j,0] = (0.299*self.rgb[i,j,0] + 0.587*self.rgb[i,j,1] + 0.114*self.rgb[i,j,2])
                self.yiq[i,j,1] = (0.596*self.rgb[i,j,0] - 0.275*self.rgb[i,j,1] - 0.321*self.rgb[i,j,2])
                self.yiq[i,j,2] = (0.212*self.rgb[i,j,0] - 0.523*self.rgb[i,j,1] + 0.311*self.rgb[i,j,2])

        return self.yiq

    def showConvYiq(self, yiq):
        plt.imshow(yiq)
        plt.show()
   
    def YIQtoRGB(self, yiq):
        new_rgb = np.zeros(yiq.shape, dtype = int)
        for i in range(len(new_rgb)):
            for j in range(len(new_rgb[i])):
                new_rgb[i,j,0] = (1.000*yiq[i,j,0] + 0.956*yiq[i,j,1] + 0.621*yiq[i,j,2])
                new_rgb[i,j,1] = (1.000*yiq[i,j,0] - 0.272*yiq[i,j,1] - 0.647*yiq[i,j,2])
                new_rgb[i,j,2] = (1.000*yiq[i,j,0] - 1.106*yiq[i,j,1] + 1.703*yiq[i,j,2])

        return np.clip(new_rgb, a_min=0, a_max=255)

    def showConvRgb(self, rgb):
        plt.imshow(rgb)
        plt.show()