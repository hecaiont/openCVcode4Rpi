import cv2
import threading

from dual_capture import camThread

from datetime import datetime



if __name__=='__main__':
    # Create two threads as follows

    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))

    thread3 = camThread("Second_Cam", 4)
    thread4 = camThread("Second_Cam", 6)
    thread1 = camThread("First_Cam", 0)
    thread2 = camThread("First_Cam", 2)

    thread1.start()
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
    thread2.start()
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
    thread3.start()
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
    thread4.start()
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
