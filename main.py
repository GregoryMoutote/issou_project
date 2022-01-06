from MediaPipeThread import MediaPipeThread
from Stage import Stage

stage = Stage("saves/test/test.issou")
stage.display_test()

detection = MediaPipeThread()
detection.start()