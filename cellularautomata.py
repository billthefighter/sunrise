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
runrule = 3
#RGB on and off color values
onColor = [0,0,100]
offColor = [0,255,0]

#atexit.register(clearOnExit)
class CellularAutomata(SampleBase):
	def __init__(self, *args, **kwargs):
		super(CellularAutomata, self).__init__(*args, **kwargs)

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
		#print(steps)
		seed=[1]
		for x in range(0,steps):
			seed.append(random.randint(0,1))
			pass
		#seed = ([0] * steps) + seed + ([0] * steps)
		#print seed
		result = seed[:]
		for i in range(steps):#----------------------------------------Change this For to a while loop, which will keep it looping until interrupt
			seed = self.step(seed, rule, k=k, r=r)
			result += seed[:]
			#----------------------------------------At this point, I want to append 
		#print result
		return result, (len(seed), steps + 1)

	def nextRun(self,rule, steps, matrix, seed=[1], k=2, r=1):
		for i in range(steps+1):
			matrix.pop(0)
		seed = self.step(matrix[0:steps+1], rule, k=k, r=r)
		matrix += seed[:]
		#print result
		return matrix, (len(seed), steps + 1)
		
	def drawLEDs(self,matrix, dimensions,canvas):
		dimensions=dimensions+1
		#this is some code for printing out matrix on the command line
		for y in range(dimensions):
			for x in range(dimensions):
				
				if matrix[y * (dimensions) + x] == 1:
				#	sys.stdout.write('X')
					canvas.SetPixel(y, x, onColor[0], onColor[1], onColor[2])
				else:
				#	sys.stdout.write(' ')
					canvas.SetPixel(y, x, offColor[0], offColor[1], offColor[2])
				#print matrix[y * (dimensions) + x],
			print " "
		print " "
		offsetCanvas = self.matrix.SwapOnVSync(canvas)
		#for y in range(dimensions):
		#	for x in range(dimensions):
		#		print x," ",y," ",y * (dimensions) + x," ",matrix[y * (dimensions) + x]
		#	print " "
	def Run(self):
		runrule=30
		lines=32
		print "run has been called"
		offsetCanvas = [1]
		offsetCanvas = self.matrix.CreateFrameCanvas()

		result, dims = self.basicRun(runrule, lines)
		self.drawLEDs(result, lines, offsetCanvas)
		while 1:
			self.nextRun(runrule, lines, result)
			#showResult(result, dims)
			self.drawLEDs(result, lines,offsetCanvas)
			time.sleep(0.015)

if __name__ == "__main__":
    parser = CellularAutomata()
    if (not parser.process()):
        parser.print_help()
	#for x in [30,90,54,110]:
	#runTest(x,32)
	#pass