from playerDetection.MediaPipeThread import MediaPipeThread
import time

eye = MediaPipeThread()
eye.start()
for i in range (10):
    time.sleep(1)
    print("ca continue...")

eye.end()