from PIL import Image,ImageDraw
import interpolators as interp

lin = Image.new("RGB",(300,100),"white")

linterp = interp.CosineInterpolator((40,3/4,70),(70,1/4,30))

for x in range(lin.width):
    lin.putpixel((x,int(linterp(x/lin.width))),0)

lin.save("cotest.png")