import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class CCube:
	def __init__(self):
		pygame.init()
		self.display = (400,400)
		pygame.display.set_mode(self.display, DOUBLEBUF|OPENGL)
		gluPerspective(80, (self.display[0]/self.display[1]), 0.1, 50.0)
		glTranslatef(0.0, 0.0, -5)
		self.vertices = (
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
	
	def view(self):
		done = False
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
					break

			keys = pygame.key.get_pressed()
			if keys[K_LEFT]:
				glRotatef(1, -1, 0, 0)
			if keys[K_RIGHT]:
				glRotatef(1, 1, 0, 0)
			if keys[K_UP]:
				glRotatef(1, 0, -1, 0)
			if keys[K_DOWN]:
				glRotatef(1, 0, 1, 0)
			if keys[K_1]:
				glRotatef(1, 0, 0, -1)
			if keys[K_2]:
				glRotatef(1, 0, 0, 1)
							
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			self.Cube()
			pygame.display.flip()
			pygame.time.wait(10)
		
		pygame.quit()
	
if __name__ == '__main__':
	c = CCube()
	c.view()
