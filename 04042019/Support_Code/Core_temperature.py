import os


def checkCoreTemperature():
    os.system('/opt/vc/bin/vcgencmd measure_temp > Cash/fileCoreTemperature.txt')
    with open('Cash/fileCoreTemperature.txt') as __fileRead:
        try:
            __temperature = float(__fileRead.read().split('=')[1].split(".")[0])
        except Exception:
            __temperature = 90
        print('__temperature =', __temperature)
        if (__temperature > 60):
            print("Dangerouse temperature")
            if (__temperature > 90):
                print("Not work temperature")
        else:
            print("Normal temperature")
        return __temperature


checkCoreTemperature()
