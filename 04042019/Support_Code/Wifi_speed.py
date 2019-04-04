import os

def checkWifiSpeed():
    os.system('cat /sys/class/net/eth0/speed > Cash/fileWifiSpeed.txt')
    
    with open('Cash/fileWifiSpeed.txt', encoding='utf-8') as __fileRead:
        __agreement = str(__fileRead.read())
        print('__agreement =', __agreement)
        if(int(__agreement) > 50):
            print('Good signal =', __agreement)
        else:
            print('No good signal', __agreement)
    # return __agreement
checkWifiSpeed()
