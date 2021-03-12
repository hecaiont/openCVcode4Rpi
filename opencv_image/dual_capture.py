import cv2
import threading

from datetime import datetime


def camPreview(previewName, camID):
    cam = cv2.VideoCapture(camID)

    ret, image = cam.read()
    print(str(ret))

    if ret:
        cv2.imwrite('./image/'+str(previewName)+'_'+str(camID)+'_'+str(datetime.utcnow().strftime('%M-%S-%f'))+'.jpg', image)
        cam.release()



class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)



if __name__=='__main__':
    # Create two threads as follows
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))

    thread1 = camThread("Camera_1", 0)
    thread2 = camThread("Camera_2", 2)
    thread1.start()
    thread2.start()

