#!/usr/bin/python
# David Zuccaro 11/06/2016

import sys
from sys import maxint
import pygame
from pygame.locals import *
import math

class turtle():

	def __init__(self, xpos, ypos, orientation, line_color):
		self.x = xpos
		self.y = ypos

		self.minx = maxint
		self.miny = maxint
		self.maxx = -maxint
		self.maxy = -maxint
		self.direction = orientation
		self.lcolor = line_color
		
		#create the screen
		self.window = pygame.display.set_mode((1900, 1200)) 
		#self.screen = pygame.display.get_surface()
		pygame.display.set_caption("Levy C Curve Fractal Variation")
	
	def move(self, length):
		rads = 0.017453293
		newx = self.x + length * math.sin(self.direction * rads)
		newy = self.y - length * math.cos(self.direction * rads)
		
		if newx < self.minx:
			self.minx = newx
			 
		if newy < self.miny:
			self.miny = newy 
			
		if newx > self.maxx:
			self.maxx = newx
			 
		if newy > self.maxy:
			self.maxy = newy
		
		pygame.draw.aalines(self.window, self.lcolor, True, [[self.x, self.y], [newx, newy]], 1)
		self.x = newx 
		self.y = newy	

	def ccurve(self, length, n, adjustment1, adjustment2):		
		fct = math.pow(2, -0.5)
		
		if n > 0:
			if n == adjustment1:
				self.direction = self.direction + 42
				self.ccurve(length * fct, n-1, adjustment1, adjustment2) 
				self.direction = self.direction - 90
				self.ccurve(length * fct, n-1, adjustment1, adjustment2) 
				self.direction = self.direction + 45
			elif n == adjustment2:
				self.direction = self.direction + 47
				self.ccurve(length * fct, n-1, adjustment1, adjustment2) 
				self.direction = self.direction - 90
				self.ccurve(length * fct, n-1, adjustment1, adjustment2) 
				self.direction = self.direction + 45
			else:
				self.direction = self.direction + 45
				self.ccurve(length * fct, n-1, adjustment1, adjustment2) 
				self.direction = self.direction - 90
				self.ccurve(length * fct, n-1, adjustment1, adjustment2) 
				self.direction = self.direction + 45			
		else:
			self.move(length)

yinit = 600
xinit = 1000

pygame.init() 

for a in range(0,17):
	for b in range(0,17):

		#create a turtle facing down.
		worker = turtle(xinit,yinit, 0 , (0,255,0)) 

		length = 200

		n = 17

		worker.ccurve(length, n, a, b)

		ratio1 =  (worker.maxx - worker.minx) / 1900
		ratio2 =  (worker.maxy - worker.miny) / 1000

		length = length / ( ratio1 if ratio1 > ratio2 else ratio2)

		worker = turtle(xinit, yinit, 0, (0,255,0))
		worker.ccurve(length, n,a, b)

		print "miny: {0}\n".format(worker.miny)
		print "maxy: {0}\n".format(worker.maxy)

		xdiff = 0
		if worker.minx < 0:
			xdiff = worker.minx
		elif worker.maxx > 1900:
			xdiff = worker.maxx - 1900

		x1 = xinit - xdiff
			
		y1 = yinit
		if worker.miny < 0:
			ydiff = worker.miny
		elif worker.maxy > 1000:
			ydiff = worker.maxy - 1000

		y1 = yinit - ydiff

		worker2 = turtle(x1, y1, 0, (0,255,0))
		worker2.ccurve(length, n,a, b)

		#draw it to the screen
		#pygame.display.flip() 

		pygame.image.save(worker2.window,"test{0:03d}-{1:03d}.png".format(a,b))

#while True:
	#for event in pygame.event.get():	
		## only look for keyboard input		
		#if not hasattr(event, 'key'):			
			#continue				

		#if event.key == K_ESCAPE:
			#sys.exit(0) # quit the game 
