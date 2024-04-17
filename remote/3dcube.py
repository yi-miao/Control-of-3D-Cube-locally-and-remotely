from multiprocessing import Process, Queue
import logging
from colorcube import ColorCube
from receiver import Receiver
	
def main():
	logger = logging.getLogger(__name__)
	logging.basicConfig(filename='server.log', level=logging.DEBUG)
	
	logger.info('3D Color Cube demo begin.')
	c = ColorCube()		# create an instance of the class (view) 
	r = Receiver()		# create an instance of the class (control)
	q = Queue()			# paramters to pass between two processes
	Process(target=c.show, args=(q,)).start() 	# member func of view with param
	Process(target=r.start, args=(q,)).start()	# member func of ctrl with param
	logger.info('3D Color Cube demo end.')
	
if __name__ == '__main__':
	main()
	

	
