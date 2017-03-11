from PIL import Image,ImageDraw
import interpolators as interp
import types
from random import random

print(types)

color = types.Color

lin = Image.new("RGB",(300,100),"white")
lindr = ImageDraw.Draw(lin)

vals = [(0,color(255,0,0)),(100,color(0,255,0)),(200,color(0,0,255)),(300,color(255,0,0))]

linterp = interp.LinearInterpolator(*vals)

for x in range(lin.width):
    lindr.line([x,0,x,lin.height],linterp(x).rgbstr)

lin.save("gradtest.png")