import threading
from PlayerDetection.MediapipeTool import MediapipeTool

class MediapipeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.media_pipe = MediapipeTool()
        self.go_on = True
        self.full_detection = False

    def run(self):
        self.media_pipe.init_hand_capture()
        while self.go_on:
            if self.full_detection:
                self.media_pipe.complete_hand_detection()
            else:
                self.media_pipe.hand_detection()



    def end_detection(self):
        self.go_on = False
        self.media_pipe.close_camera()
