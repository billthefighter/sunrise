from PIL import Image
from PIL import ImageOps
import random
#from rgbmatrix import Adafruit_RGBmatrix
import atexit
import time
#define inputs
#from rgbmatrix import RGBMatrix

#matrix = Adafruit_RGBmatrix(32, 1)

#def clearOnExit():
#    matrix.Clear()

#atexit.register(clearOnExit)

#---------------------------------- need to create a class that defines a canvas array so I can 
class canvasCellularAut():
    def __init__(self):
        self.display = [[0 for y in range(32)] for x in range(32)]
    def scroll(self,pop):
        self.display.pop(0)
        self.display.append(pop)
    def draw(self):
        #add stuff here
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
        #print scrollinglife.display
        showResult(scrollinglife.display,(32,32)) 
        stream = []
        for x in xrange(32):
            for y in xrange(32):
                stream.append(scrollinglife.display[x][y])
                pass
            pass
        print stream
        showResult(stream, (32,32))
        #----------------------------------------At this point, I want to append 
    #return result, (len(seed), steps + 1)
    
#def printRowToMatrix(pumpoutrow):
    #return


def showResult(result, dims, k=2):
    i = Image.new("L", dims)
    i.putdata(result, (255 / (k - 1)))
    i = i.crop(i.getbbox())
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