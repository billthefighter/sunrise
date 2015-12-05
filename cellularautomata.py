from PIL import Image
from PIL import ImageOps
from samplebase import SampleBase
import random
import atexit
import time
from rgbmatrix import RGBMatrix
import argparse
#define inputs
#from rgbmatrix import RGBMatrix

#matrix = Adafruit_RGBmatrix(32, 1)

#def clearOnExit():
#    matrix.Clear()

#atexit.register(clearOnExit)

#---------------------------------- need to create a class that defines a canvas array so I can 
# class displayobject(SampleBase):
#     def __init__(self, *args, **kwargs):
#         super(displayobject, self).__init__(*args, **kwargs)
    
#     def Run(self,displaymatrix):
#         offsetCanvas = self.matrix.CreateFrameCanvas()
#         for x in xrange(len(displaymatrix)):
#             for y in xrange(len(displaymatrix)):
#                 blockvalue = displaymatrix[x][y]
#                 print blockvalue
#                 offsetCanvas.SetPixel(x, y, blockvalue*255, blockvalue*255, blockvalue*255)
#                 pass
#             pass
class displayobject():
    def __init__(self, *args, **kwargs):
        self.add_argument("-r", "--rows", action = "store", help = "Display rows. 16 for 16x32, 32 for 32x32. Default: 32", default = 32, type = int)
        self.add_argument("-P", "--parallel", action = "store", help = "For Plus-models or RPi2: parallel chains. 1..3. Default: 1", default = 1, type = int)
        self.add_argument("-c", "--chain", action = "store", help = "Daisy-chained boards. Default: 1.", default = 1, type = int)
        self.add_argument("-p", "--pwmbits", action = "store", help = "Bits used for PWM. Something between 1..11. Default: 11", default = 11, type = int)
        self.add_argument("-l", "--luminance", action = "store_true", help = "Don't do luminance correction (CIE1931)")
        self.add_argument("-b", "--brightness", action = "store", help = "Sets brightness level. Default: 100. Range: 1..100", default = 100, type = int)
        self.args = {}
        self.matrix = RGBMatrix(self.args["rows"], self.args["chain"], self.args["parallel"])
        self.matrix.pwmBits = self.args["pwmbits"]
        self.matrix.brightness = self.args["brightness"]
        self.matrix.CreateFrameCanvas()
    def Run(self):

        for x in xrange(len(displaymatrix)):
            for y in xrange(len(displaymatrix)):
                blockvalue = displaymatrix[x][y]
                print blockvalue
                offsetCanvas.SetPixel(x, y, blockvalue*255, blockvalue*255, blockvalue*255)
                pass

class canvasCellularAut():
    def __init__(self):
        self.display = [[0 for y in range(32)] for x in range(32)]
    def scroll(self,pop):
        self.display.pop(0)
        self.display.append(pop)
    def draw(self):
        canvas = displayobject()
        canvas.Run(self.display)
        return

    #def pop(self): #pops latest result value into display matrix

def step(a, rule, k=2, r=1):
    nbrs = [a[c:] + a[:c] for c in range(-r, r+1, 1)]
    #print "numbers"
    #print nbrs
    l = []
    for t in apply(zip, nbrs):
        result = 0
        for i in t:
            result = (result * k) + i
        l.append(result)
    return [((rule / (k ** v)) % k) for v in l]

def basicRun(rule, steps, stepper, seed=[1], k=2, r=1):
    #print steps
    seed=[1]
    poop = 0
    for x in xrange(0,steps):
        seed.append(random.randint(0,1))
        pass
    #seed = ([0] * steps) + seed + ([0] * steps)
    #print seed
    result = seed[:]
    #for i in range(steps):#----------------------------------------Change this For to a while loop, which will keep it looping until interrupt
    scrollinglife = canvasCellularAut()
    while poop < 10:
        seed = stepper(seed, rule, k=k, r=r)
        result += seed[:]
        pumpoutrow = seed[:]
        scrollinglife.scroll(pumpoutrow)
        poop += 1
        scrollinglife.draw()
        #----------------------------------------At this point, I want to append 
    #return result, (len(seed), steps + 1)


def showResult(result, dims, k=2):
    i = Image.new("L", dims)
    i.putdata(result, (255 / (k - 1)))
    #i = i.crop(i.getbbox())
    i = ImageOps.invert(i)
    i.load()
    i.show()
    #matrix.SetImage(i.im.id, 0, 0)
    time.sleep(1)

def runTest(runrule,lines):
    result, dims = basicRun(runrule, lines, step)
    #showResult(result, dims)

if __name__ == "__main__":
    runTest(30,32)
    #for x in [30,90,54,110]:
        #runTest(x,32)
        #pass