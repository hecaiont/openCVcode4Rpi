import numpy as np
import cv2
import time
from datetime import datetime
from multiprocessing import Process, Event


def videoPreview(previewName, camID, duration):
    cap = cv2.VideoCapture(camID)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(str(previewName)+'_'+str(camID)+'_'+str(datetime.utcnow().strftime('%M-%S-%f'))+'.avi', fourcc, 20.0, (640,480))

    timeout = time.time() + int(duration)   # duration sec from now
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame,0)
            # write the flipped frame
            out.write(frame)

        else:
            break

        if time.time() > timeout: # break if duration over
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return


def task(event, cam_params):
    e.wait()  # Wait for an event
    videoPreview(cam_params[0], cam_params[1], cam_params[2])

if __name__ == '__main__':
    e = Event()  # Create event that will be used for synchronization
    
    #IR
    p1 = Process(target=task, args=(e, ["First_Cam", 0, 5]))
    p1.start()
    
    #RGB
    p2 = Process(target=task, args=(e, ["First_Cam", 2, 5]))
    p2.start()
    
    #IR
    p3 = Process(target=task, args=(e, ["Second_Cam", 4, 5]))
    p3.start()
    
    #RGB
    p4 = Process(target=task, args=(e, ["Second_Cam", 6, 5]))
    p4.start()

    e.set()  # Set event so all processes can start at the same time

