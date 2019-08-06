
import matplotlib.image as image
import matplotlib.pyplot as plt
from IPython.display import Image
import webbrowser
from convert import Convert
from tones import Tones
from negative import Negative, NegativeUnchanged, NegativeYiq
from bright import Bright
import numpy as np

class Image (Convert, Tones, Negative, NegativeUnchanged, NegativeYiq, Bright):
    def __init__(self,name):
        self.name = name
        self.rgb = (image.imread(self.name)) #Recive RGB values
        self.yiq = np.zeros(self.rgb.shape) #Create with zeros

    def showImageRgb(self): 
        plt.imshow(self.rgb)
        plt.show()
    
    def showValueRgb(self):
        arquivo = open("RGB_value.txt", 'w')
        arquivo.write(str(self.rgb))
        arquivo.close()
        webbrowser.open("RGB_value.txt")