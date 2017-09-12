from rplidar import RPLidar
import os
import matplotlib.pyplot as plt
import numpy as np


def main():
    if 'linux' in os.name.lower():
        lidar = RPLidar('/dev/ttyUSB0')
    else:
        lidar = RPLidar('com3')
    # print(info(lidar))
    # print(health(lidar))
    lidar.stop_motor()
    while 1 == 1:
        print('----------------------------------------------')
        print('1: Start Motor\n'
              '2: Stop Motor\n'
              '3: Start Scan\n'
              '4: Stop Scan\n'
              '5: Exit')
        ans = input('Please Enter Menu Number: ')
        if ans is '1':
            start(lidar)
        elif ans is '2':
            stop(lidar)
        elif ans is '3':
            scan(lidar)
        elif ans is '4':
            print('4')
        elif ans is '5':
            break
        else:
            print('Invalid Option')

            # for i, scan in enumerate(lidar.iter_scans()):
            #     print('%d: Got %d measurments' % (i, len(scan)))
            #     if i > 10:
            #         break


def start(lidar):
    lidar.start_motor()


def stop(lidar):
    lidar.stop_motor()


def info(lidar):
    return lidar.get_info()


def health(lidar):
    return lidar.get_health()


def scan(lidar):

    start(lidar)
    i = 0
    r = []
    th = []

    # start data collection

    for scans in lidar.iter_scans():
        for mes in scans:
            r.append(mes[1]*np.pi/180)
            r.append(0)
            th.append(mes[2])
            th.append(0)
        print(scans)
        i = i + 1
        if i is 60:
            break
    stop(lidar)
    # sorted(r, key=lambda theta: theta[0])
    # for x in len(r):
    #     r(x-1)-r(x-2)
    # print(r)
    graph = plt.subplot(111, projection='polar')
    c = plt.polar(r, th, c='k', linewidth=0.01)
    plt.axis('off')
    plt.show()
if __name__ == '__main__':
    main()
