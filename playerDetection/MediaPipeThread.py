from playerDetection.MediaPipeTool import MediaPipeTool
import threading

class MediaPipeThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.mediaPipeClass = MediaPipeTool()
        self._stopevent = threading.Event()

    def run(self):
        self.mediaPipeClass.body_detection()

    def stop(self):
        self._stopevent.set()