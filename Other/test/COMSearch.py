import serial
def Search(_baundrate = 115200):

    _COM = ['COM' + str(i) for i in range(1, 5)]

    for COM in _COM:
        try:
            port = serial.Serial(port=COM, \
                                 baudrate=_baundrate, \
                                 parity=serial.PARITY_NONE, \
                                 stopbits=serial.STOPBITS_ONE, \
                                 bytesize=serial.EIGHTBITS, \
                                 timeout=0)
            while True:
                if len(port.readline()) != 0:
                    print(len(port.readline()))
                else:
                    print("pass")
                    break

        except Exception as e:
            print(e)
            continue
