from PIL import Image,ImageDraw
import interpolators as interp
from random import random

cos = Image.new("RGB",(300,100),"white")
cosdr = ImageDraw.Draw(cos)

lin = Image.new("RGB",(300,100),"white")
lindr = ImageDraw.Draw(lin)

cu = Image.new("RGB",(300,100),"white")
cudr = ImageDraw.Draw(cu)

vals = [(x/10,random()*100) for x in range(11)]

costerp = interp.CosineInterpolator(*list(map(lambda x: (x[0]*cos.width,x[1]),vals)))
linterp = interp.LinearInterpolator(*list(map(lambda x: (x[0]*lin.width,x[1]),vals)))
cuterp = interp.CubicInterpolator(*list(map(lambda x: (x[0]*cu.width,x[1]),vals)))

for x in range(cos.width-1):
    cosdr.line([x,costerp(x),x+1,costerp(x+1)],"black")
    lindr.line([x,linterp(x),x+1,linterp(x+1)],"black")
    cudr.line([x,cuterp(x),x+1,cuterp(x+1)],"black")

cos.save("cotest.png")
lin.save("lintest.png")
cu.save("cutest.png")