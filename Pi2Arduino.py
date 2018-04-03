import serial
import time

ser = serial.Serial("/dev/ttyUSB0",9600, timeout=5)
time.sleep(3) #wait for connection to complete

while True:
    print("Sending: blue")
    ser.write("blue\n".encode("utf-8"))
    time.sleep(1)
    print("Received: ", ser.readline().decode("utf-8"))
    
    print("Sending: green")
    ser.write("green\n".encode("utf-8"))
    time.sleep(1)
    print("Received: ", ser.readline().decode("utf-8"))
    
    print("Sending: red")
    ser.write("red\n".encode("utf-8"))
    time.sleep(1)
    print("Received: ", ser.readline().decode("utf-8"))
    