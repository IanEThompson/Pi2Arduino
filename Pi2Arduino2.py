import serial
import time

ser = serial.Serial("/dev/ttyUSB0",9600, timeout=2)
time.sleep(3) #wait for connection to complete

while True:
    sendString = input(">>")
    print("Sending: ", sendString)
    ser.flush()
    ser.write((sendString + "\n").encode("utf-8"))
    time.sleep(1)
    print("Received: ", ser.readline().decode("utf-8"))
    
