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
image.showTones(image.choiceTone(0))
image.showTones(image.choiceTone(1))
image.showTones(image.choiceTone(2))
image.showTones(image.RGBtone())

# Separating and Inverting (NEGATIVE)
image.showTones(image.choiceNegTone(0))
image.showTones(image.choiceNegTone(1))
image.showTones(image.choiceNegTone(2))
image.showTones(image.RGBNtone())

#Inverting only one chanel, the othrs remain unchanged
image.showTones(image.choiceNegUnchTone(0))
image.showTones(image.choiceNegUnchTone(1))
image.showTones(image.choiceNegUnchTone(2))

#YIQ Negative
#We make the "negative" of Y in YIQ and convert to RGB
y_negativo = image.YNtone()
rgb_from_yiq_neg = image.YIQtoRGB(y_negativo)
image.showConvRgb(rgb_from_yiq_neg)

#Bright
image.showMult(image.multiplicativeRgb(0,1.2))
image.showMult(image.multiplicativeRgb(1,1.2))
image.showMult(image.multiplicativeRgb(2,1.2))
image.showMult(image.multiplicativeYiq(2))


