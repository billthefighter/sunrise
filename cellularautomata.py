#! python2.7
from PIL import Image
from PIL import ImageOps
import random
import sys
#from rgbmatrix import Adafruit_RGBmatrix
import atexit
import time
from samplebase import SampleBase
#define inputs
#self.rule = 3
#RGB on and off color values
onColor = [120,0,255]
offColor = [0,255,120]
length = 64 #(length of panels)
#Cool Rules: 30,90,54,110
startrule = 30

#atexit.register(clearOnExit)
#class array:
#	def __init__(self,dimensions):
#		self.xdim = 32 
#		self.ydim =




class CellularAutomata(SampleBase):
	def __init__(self, *args, **kwargs):
		super(CellularAutomata, self).__init__(*args, **kwargs)
		self.oncolor = onColor
		self.offcolor = offColor
		self.state = []
		self.width = 0
		self.length = length
		self.rule = startrule

	def step(self,a, rule, k=2, r=1):
		nbrs = [a[c:] + a[:c] for c in range(-r, r+1, 1)]
		l = []
		for t in apply(zip, nbrs):
			result = 0
			for i in t:
				result = (result * k) + i
			l.append(result)
		return [((rule / (k ** v)) % k) for v in l]

	def basicRun(self,rule, steps, seed=[1], k=2, r=1):
		#print "steps"
		#print(steps)
		seed=[1]
		seed = ([0] * 15) + seed + ([0] * 16)
		#for x in range(0,steps):
		#	seed.append(random.randint(0,1))
		#	pass
		#seed = ([0] * steps) + seed + ([0] * steps)
		#print seed
		#result = seed[:]
		#for i in range(steps):#----------------------------------------Change this For to a while loop, which will keep it looping until interrupt
		#	seed = self.step(seed, rule, k=k, r=r)
		#	result += seed[:]
			#----------------------------------------At this point, I want to append 
		#print result
		result = [seed[:]]
		for i in range(steps):#----------------------------------------Change this For to a while loop, which will keep it looping until interrupt
			seed = self.step(seed, rule, k=k, r=r)
			result.append(seed[:])
		#print result
		self.state = result
		self.width = len(result)
		return result, (len(seed), steps + 1)

	def nextRun(self,rule, steps, matrix, seed=[1], k=2, r=1):
		#for i in range(steps+1):
		#	matrix.pop(0)
		matrix.pop(0)
		#print "self.length"
		#print len(matrix)
		seed = self.step(matrix[len(matrix)-1][:], rule, k=k, r=r)
		matrix.append(seed[:])
		#print result
		#print matrix
		#self.oncolor = [(self.oncolor[0] + 1) % 255,(self.oncolor[1] + 1) % 255,(self.oncolor[2] + 1) % 255]
		#self.offcolor = [(self.offcolor[0] + 1) % 255, (self.offcolor[1] + 1) % 255, (self.offcolor[2] + 1) % 255]
		return matrix, (len(seed), steps + 1)
		
	def drawLEDs(self,matrix, dimensions,canvas):
		#dimensions=dimensions+1
		#this is some code for printing out matrix on the command line
		#print "dimensions"
		#print dimensions
		#print "matrix"
		#print matrix
		#canvas.SetPixel(16, 16, 0, 0, 255)
		#canvas.SetPixel(0, 16, 0, 255, 0)
		#canvas.SetPixel(1, 16, 255, 0, 0)
		#canvas.SetPixel(1, 2, 0, 255, 255)
		#offsetCanvas = self.matrix.SwapOnVSync(canvas)
		#time.sleep(10)	
		#print "len(matrix[0])"
		#print len(matrix[0])
		#print "len(matrix)"
		#print len(matrix)-1
		for x in xrange(len(matrix)):
			for y in xrange(len(matrix[0])):
				#print "x"
				#print x
				#print "y"
				#print y
				if matrix[x][y] == 1:
					#print x
					#sys.stdout.write('X')
					canvas.SetPixel(x, y, self.oncolor[0], self.oncolor[1], self.oncolor[2])
					#canvas.SetPixel(y, x, onColor[0], onColor[1], onColor[2])
				else:
					#sys.stdout.write(' ')
					#canvas.SetPixel(y, x, offColor[0], offColor[1], offColor[2])
					canvas.SetPixel(x, y, self.offcolor[0], self.offcolor[1], self.offcolor[2])
				#print matrix[y * (dimensions) + x],
				#time.sleep(.01)	
			#print " "
		#print " "
		offsetCanvas = self.matrix.SwapOnVSync(canvas)
		#for y in range(dimensions):
		#	for x in range(dimensions):
		#		print x," ",y," ",y * (dimensions) + x," ",matrix[y * (dimensions) + x]
		#	print " "
	def Run(self):
		#lines=32
		print "run has been called"
		offsetCanvas = [1]
		offsetCanvas = self.matrix.CreateFrameCanvas()

		self.basicRun(self.rule, self.length)
		#self.drawLEDs(self.state, self.width, offsetCanvas)
		ticker = 0
		while 1:
			self.drawLEDs(self.state, self.width, offsetCanvas)
			self.nextRun(self.rule, self.length, self.state)
			#showResult(result, dims)
			#self.drawLEDs(self.state, lines,offsetCanvas)
#--------------------------------------------Ticker for changing rules			
			#if ticker == 64:
			#	self.rule = 
			#	pass
			#else:
			#	ticker +=1
			#	pass
			time.sleep(0.015)
			#time.sleep(1)

if __name__ == "__main__":
    parser = CellularAutomata()
    if (not parser.process()):
        parser.print_help()
	#for x in [30,90,54,110]:
	#runTest(x,32)
	#pass
