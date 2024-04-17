import serial

class Receiver():
	def __init__(self):
		self.ser = serial.Serial(
		    port="/dev/ttyS0", 
		    baudrate=115200, 
		    bytesize=serial.EIGHTBITS, 
		    parity=serial.PARITY_NONE,
		    stopbits=serial.STOPBITS_ONE,
		    timeout=2, 
		)
		self.DATA_FRAME_LENGTH = 32

	def start(self, q=None):
		while True:
			frame = bytearray()
			received_data = None
			try:
				received_data = self.ser.read()
				if received_data:
					intReceived = int.from_bytes(received_data, byteorder='little')
					if intReceived == self.DATA_FRAME_LENGTH:
						frame.extend(received_data)
						nextBytes = self.ser.read(self.DATA_FRAME_LENGTH-1)
						frame.extend(nextBytes)
						
						ch1byte = bytearray()
						ch1byte.append(frame[2])
						ch1byte.append(frame[3])
						ch1 = int.from_bytes(ch1byte, byteorder='little')
						
						ch2byte = bytearray()
						ch2byte.append(frame[4])
						ch2byte.append(frame[5])
						ch2 = int.from_bytes(ch2byte, byteorder='little')
						
						ch3byte = bytearray()
						ch3byte.append(frame[6])
						ch3byte.append(frame[7])
						ch3 = int.from_bytes(ch3byte, byteorder='little')
						
						ch4byte = bytearray()
						ch4byte.append(frame[8])
						ch4byte.append(frame[9])
						ch4 = int.from_bytes(ch4byte, byteorder='little')
						
						ch5byte = bytearray()
						ch5byte.append(frame[10])
						ch5byte.append(frame[11])
						ch5 = int.from_bytes(ch5byte, byteorder='little')
						
						ch6byte = bytearray()
						ch6byte.append(frame[12])
						ch6byte.append(frame[13])
						ch6 = int.from_bytes(ch6byte, byteorder='little')
						
						# print("ch1=", ch1, "ch2=", ch2, "ch3=", ch3)
		                
						if q:
							co = []
							co.append(ch1)
							co.append(ch2)
							co.append(ch3)
							q.put(co)
		
					else:
						pass
			except serial.SerialException as e:
				print(f"SerialException: {str(e)}")
	        
if __name__ == '__main__':
    r = Receiver()
    r.start()


