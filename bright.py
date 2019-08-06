import matplotlib.image as image
import matplotlib.pyplot as plt
from IPython.display import Image
import numpy as np

class Bright():
	def multiplicativeRgb(self,rgb,c):
		val = np.copy(self.rgb)
		val[:,:,rgb] = np.multiply(val[:,:,rgb],c)
		return np.clip(val, a_min=0, a_max=255)

	def multiplicativeYiq(self,c):
		val = np.copy(self.yiq)
		val[:,:,0] = np.multiply(val[:,:,0],c)
		return np.clip(val, a_min=0, a_max=255)

	def showMult(self, mult):
		plt.imshow(mult)
		plt.show()
