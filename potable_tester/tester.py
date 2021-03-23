# tester

import time 
import subprocess
from multiprocessing import Process, Event

from opencv_video.cmmnd_single_module_capture import videoPreview



class Test:

    def __init__(self):
        self.time = time.time()

    def task_mic(self):
        self.e.wait()  # Wait for an event
        self.record = subprocess.run('./ultra_mic/cmmnd_record250k.sh') # 3sec

    def task_cam(self, event, cam_params):
        self.e.wait()  # Wait for an event
        videoPreview(cam_params[0], cam_params[1], cam_params[2])


    def run(self):
        self.e = Event()  # Create event that will be used for synchronization
    
        #Ultra Mic
        p0 = Process(target=self.task_mic, args=())
        p0.start()

        #IR
        p1 = Process(target=self.task_cam, args=(self.e, ["First_Cam", 0, 3]))
        p1.start()

        #RGB
        p2 = Process(target=self.task_cam, args=(self.e, ["First_Cam", 2, 3]))
        p2.start()

        self.e.set()  # Set event so all processes can start at the same time

