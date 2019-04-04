import os

def activationCamera():
    __agreement = os.system(' > Cash/fileCameraActivation.txt') # команда для включения камеры

    with open('Cash/fileCameraActivation.txt', encoding='utf-8') as __fileRead:
        __agreement = str(__fileRead.read())
        try:
            print('__agreement', __agreement)
        except Exception:
            __agreement = 1;
        if (__agreement == 0):
            print('Camera active')
        else:
            print('Camera error')
    return __agreement


activationCamera()
