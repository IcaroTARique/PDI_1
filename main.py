#!/usr/bin/python3.6
import sys
from read_img import Image

image = Image(sys.argv[1])
image.showImageRgb()
image.showValueRgb()

# Converting RGB to YIQ
yiq = image.RGBtoYIQ()
image.showConvYiq(yiq)

# Converting YIQ to RGB
rgb = image.YIQtoRGB(yiq)
image.showConvRgb(rgb)

# Separating in tones R, G, and B
image.showTones(image.Rtone())
image.showTones(image.Gtone())
image.showTones(image.Btone())
image.showTones(image.RGBtone())

# Separating and Inverting (NEGATIVE)
image.showTones(image.RNtone())
image.showTones(image.GNtone())
image.showTones(image.BNtone())
image.showTones(image.RGBNtone())

#Inverting only one chanel, the othrs remain unchanged
image.showTones(image.RNUtone())
image.showTones(image.GNUtone())
image.showTones(image.BNUtone())

#YIQ Negative
#We make the "negative" of Y in YIQ and convert to RGB
y_negativo = image.YNtone()
rgb_from_yiq_neg = image.YIQtoRGB(y_negativo)
image.showConvRgb(rgb_from_yiq_neg)
