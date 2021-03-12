from multiprocessing import Process, Event
import os
import time

import cv2
from dual_capture import camThread
from datetime import datetime


def camPreview(previewName, camID):
    cam = cv2.VideoCapture(camID)

    ret, image = cam.read()
    print(str(ret))

    if ret:
        cv2.imwrite('./image/'+str(previewName)+'_'+str(camID)+'_'+str(datetime.utcnow().strftime('%M-%S-%f'))+'.jpg', image)
        cam.release()

def task(event, cam_params):
    proc_id = os.getpid()
    e.wait()  # Wait for an event
    camPreview(cam_params[0], cam_params[-1])



if __name__ == '__main__':
    e = Event()  # Create event that will be used for synchronization

    p1 = Process(target=task, args=(e, ["First_Cam", 0]))
    p1.start()

    p2 = Process(target=task, args=(e, ["First_Cam", 2]))
    p2.start()

    p3 = Process(target=task, args=(e, ["Second_Cam", 4]))
    p3.start()

    p4 = Process(target=task, args=(e, ["Second_Cam", 6]))
    p4.start()

    e.set()  # Set event so all processes can start at the same time
