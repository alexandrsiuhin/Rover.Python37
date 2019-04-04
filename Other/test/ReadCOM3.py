import serial
import time
def f_arduino():
    print('test arduino')

COM = "COM3"
try:
    port = serial.Serial(COM, 9600)
    time.sleep(3)
    port.read(10)

    while True:
        print(port.readline().decode("utf-8"),"***", COM)
        s = len(port.readline())
        if s != 0:
            print(s)
        else:
            print("pass")
            break
        data = port.readline().decode().split()
        command = {'arduino':f_arduino()}
        for c in command:
            if c in data:
                print(c)
                f = command[c]
                f()
                print(COM)
                break
        if('test' in data):
            print("Equal")
            print(COM)
            break

except Exception as e:
    print(e)
    pass
