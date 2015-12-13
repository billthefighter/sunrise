#! python2.7
import random
import sys
import atexit
import time
from samplebase import SampleBase
from colorsys import hls_to_rgb
from random import shuffle
from itertools import izip
#define inputs
#self.rule = 3
length = 64 #(length of panels)
#Cool Rules: 30,90,54,110
startrule = 30
luminance = 0.2
saturation = 1.0

COLORMAP_SIZE = 16

def lum2rgb(hue):
	return [x * 256 for x in hls_to_rgb(hue, luminance, saturation)]

def make_colormap(start_hue, stop_hue):
	hue_range = stop_hue - start_hue
	return map(lum2rgb, [
		start_hue + (hue_range * float(x) / COLORMAP_SIZE)
		for x in range(COLORMAP_SIZE)
	])

oncolors = make_colormap(0.2, 0.4)
oncolors += reversed(oncolors)

offcolors = make_colormap(0.6, 0.8)
offcolors += reversed(offcolors)

#atexit.register(clearOnExit)
#class array:
#	def __init__(self,dimensions):
#		self.xdim = 32 
#		self.ydim =

class CellularAutomata(SampleBase):
	def __init__(self, *args, **kwargs):
		super(CellularAutomata, self).__init__(*args, **kwargs)
		self.state = []
		self.width = 0
		self.length = length
		self.rule = startrule

	#@profile
	def step(self,a, rule, k=2, r=1):
		nbrs = [a[c:] + a[:c] for c in range(-r, r+1, 1)]
		l = []
		for t in apply(zip, nbrs):
			result = 0
			for i in t:
				result = (result * k) + i
			l.append(result)
		return [((rule / (k ** v)) % k) for v in l]
	#@profile
	def basicRun(self,rule, steps, seed=[1], k=2, r=1):
		#print "steps"
		#print(steps)
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
	#@profile
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
	#@profile
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

		r_on, g_on, b_on = self.oncolor
		def pixel_on(x, y):
			canvas.SetPixel(x, y, r_on, g_on, b_on)

		r_off, g_off, b_off = self.offcolor
		def pixel_off(x, y):
			canvas.SetPixel(x, y, r_off, g_off, b_off)

		flat_matrix = []
		for row in matrix:
			flat_matrix.extend(row)

		# Avoid recomputing the x and y values for every pixel
		# Profiling showed that about half the time was spent
		# doing the division and modulo. This computation should
		# run only once.
		if not hasattr(self, 'cached_xys'):
			self.cached_xys = []
			num_rows = len(matrix[0])
			for i in range(len(flat_matrix)):
				x = i / num_rows
				y = i % num_rows
				self.cached_xys.append((x, y))

		# Make sure the matrix didn't sneakily change size
		assert len(self.cached_xys) == len(flat_matrix)

		# Flatten out the xys to avoid a nested loop
		for (x, y), value in izip(self.cached_xys, flat_matrix):
			if value:
				pixel_on(x, y)
			else:
				pixel_off(x, y)
					#print x
					#sys.stdout.write('X')
				#print matrix[y * (dimensions) + x],
				#time.sleep(.01)	
			#print " "
		#print " "
		self.offsetCanvas = self.matrix.SwapOnVSync(canvas)
		#for y in range(dimensions):
		#	for x in range(dimensions):
		#		print x," ",y," ",y * (dimensions) + x," ",matrix[y * (dimensions) + x]
		#	print " "
	#@profile
	def Run(self):
		#lines=32
		print "run has been called"
		self.offsetCanvas = self.matrix.CreateFrameCanvas()

		self.basicRun(self.rule, self.length)
		#self.drawLEDs(self.state, self.width, offsetCanvas)

		hue = 0.0
		ticker = 0
		i = 0
		len_oncolors = len(oncolors)
		while 1:
			i = (i + 1) % len_oncolors
			self.oncolor = oncolors[i]
			self.offcolor = offcolors[i]
			self.drawLEDs(self.state, self.width, self.offsetCanvas)
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

if __name__ == "__main__":
    parser = CellularAutomata()
    if (not parser.process()):
        parser.print_help()
	#for x in [30,90,54,110]:
	#runTest(x,32)
	#pass
