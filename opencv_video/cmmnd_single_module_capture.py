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
            frame = cv2.flip(frame, 0)
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


