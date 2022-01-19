import threading
from playerDetection.MediaPipeTool import MediaPipeTool

class MediaPipeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.mediaPipe = MediaPipeTool()
        self.continuer = True
        self.fullDetection = False

    def run(self):
        self.mediaPipe.initHandCapture()
        while self.continuer:
            if self.fullDetection:
                self.mediaPipe.complete_hand_detection()
            else:
                self.mediaPipe.hand_detection()



    def endDetection(self):
        self.continuer = False
        self.mediaPipe.closeCamera()
