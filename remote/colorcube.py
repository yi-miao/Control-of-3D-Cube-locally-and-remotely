import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class ColorCube():
	def __init__(self):
		self.vertices= (
		    (1, -1, -1), #2
		    (1, 1, -1), #1
		    (-1, 1, -1), #7
		    (-1, -1, -1), #5
		    (1, -1, 1), #3
		    (1, 1, 1), #0
		    (-1, -1, 1), #6
		    (-1, 1, 1) #4
		)
		self.edges = (
		    (0,1),
		    (0,3),
		    (0,4),
		    (2,1),
		    (2,3),
		    (2,7),
		    (6,3),
		    (6,4),
		    (6,7),
		    (5,1),
		    (5,4),
		    (5,7)
		)
		self.colors = (
		    (1,0,0), #r
		    (0,1,0), #g
		    (0,0,1), #b
		    (0,1,0), #g
		    (1,1,1), #wh
		    (0,1,1), #cy
		    (1,0,0), #r
		    (0,1,0), #g
		    (0,0,1), #b
		    (1,0,0), #r
		    (1,1,1), #wh
		    (0,1,1), #cy
		)
		self.surfaces = (
		    (0,1,2,3),
		    (3,2,7,6),
		    (6,7,5,4),
		    (4,5,1,0),
		    (1,5,7,2),
		    (4,0,3,6)
		)
		self.cube = None
		self.LIMIT_LOW = 1200
		self.LIMIT_HIGH = 1800
		
	def Cube(self):
	    # render colored surfaces as quads
	    glBegin(GL_QUADS)
	    for surface in self.surfaces:
	        x = 0
	        for vertex in surface:
	            x+=1
	            glColor3fv(self.colors[x])
	            glVertex3fv(self.vertices[vertex])
	    glEnd()
	    # render lines between vertices
	    glBegin(GL_LINES)
	    for edge in self.edges:
	        for vertex in edge:
	            glVertex3fv(self.vertices[vertex])
	    glEnd()

	def show(self, q=None):
		pygame.init()
		display = (400,400)
		pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
		
		gluPerspective(80, (display[0]/display[1]), 0.1, 50.0)
		glTranslatef(0.0, 0.0, -5)
		
		done = False
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
					break

			if not q.empty():
				try:
					co = q.get()
					# print("co: ", co)
					if co[0] <= self.LIMIT_LOW:
						glRotatef(1, 0, -1, 0)
					elif co[0] >= self.LIMIT_HIGH:
							glRotatef(1, 0, 1, 0)
					elif co[1] <= self.LIMIT_LOW:
						glRotatef(1, -1, 0, 0)
					elif co[1] >= self.LIMIT_HIGH:
						glRotatef(1, 1, 0, 0)
					elif co[2] <= self.LIMIT_LOW:
						glRotatef(1, 0, 0, 1)
					elif co[2] >= self.LIMIT_HIGH:
						glRotatef(1, 0, 0, -1)
				except:
					pass
                    
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			self.cube = self.Cube()
			pygame.display.flip()
			pygame.time.wait(10)
		
		pygame.quit()
		
if __name__ == '__main__':
	from multiprocessing import Process, Queue
	q = Queue()
	g = ColorCube()
	g.show(q)
	
