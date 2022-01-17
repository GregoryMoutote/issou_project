from testMediaPipe import MediaPipeTool
import threading

class MediaPipeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.mediaPipeClass = MediaPipeTool()
    def run(self) :
        self.mediaPipeClass.body_detection()