import serial
import time


def SendinglMessgage():
    try:

        port = serial.Serial("COM3", 9600)
        time.sleep(3)
        port.read()

        while True:
            # print(port.readline().decode("utf-8"), "***", "COM3")
            s = len(port.readline())
            if s != 0:
                data = port.readline().decode().split()
                if ('MotorShield' in data):
                    print(data)
                    print("Equal")
                    return
                    break
                else:
                    print(data)
                    print("Break")
                    break
            else:
                print("pass")
                break

    except Exception as e:
        print(e)
        pass


SendinglMessgage()
