# Galih setiko
# instagram : https://instagram.com/galihstyoko

import time, os
import sys

def startTimer(**kwargs):
    if kwargs.keys() == 'hour':
        print('ini hour')
    else:
        print('Stupid')
    return

# mengidentifikasi dan memfilter inputan user
def main(value):
    if sys.argv[1] == '--timer' or sys.argv[1] == '-t':
        if sys.argv[2] == '-h' or sys.argv[2] == '--hour':
            startTimer(hour=sys.argv[3])
        elif sys.argv[2] == '-m' or sys.argv[2] == '--minute':
            startTimer(minute=sys.argv[3])
        elif sys.argv[2] == '-s' or sys.argv[2] == '--second':
            startTimer(second=sys.argv[3])
        else:
            print('Erorr comand')
            
    elif sys.argv[1] == '--alarm' or sys.argv[1] == '-a':
        print('its alarm')
    else:
        print('bad command')


if __name__ == '__main__':
    main(sys.argv)
    # try:
    #     # option = sys.argv[1]
    #     # timer = sys.argv[2]
    #     main(sys.argv)
    # except:
    #     print(f'[-] Example : {sys.argv[0]} --timer --minute 2')