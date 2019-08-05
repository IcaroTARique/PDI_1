
import matplotlib.image as image
import matplotlib.pyplot as plt
from IPython.display import Image
import webbrowser
from convert import Convert
from tones import Tones
from negative import Negative, NegativeUnchanged, NegativeYiq
import numpy as np

class Image (Convert, Tones, Negative, NegativeUnchanged, NegativeYiq):
    def __init__(self,name):
        self.name = name
        self.rgb = (image.imread(self.name))
        self.yiq = np.zeros(self.rgb.shape)

    # def readImg(self):
    #     self.rgb = image.imread(self.name)
    #     self.rgb.flags

    def showImageRgb(self): 
        plt.imshow(self.rgb)
        plt.show()
    
    def showValueRgb(self):
        arquivo = open("RGB_value.txt", 'w')
        arquivo.write(str(self.rgb))
        arquivo.close()
        webbrowser.open("RGB_value.txt")