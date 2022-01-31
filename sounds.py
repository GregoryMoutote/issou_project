from pygame import *
import cv2

mixer.init()
#mixer.music.load('musics/12.wav')
#mixer.music.set_volume(0.1)
#mixer.music.play(-1)
sound = mixer.Sound('musics/12.wav')
sound.play()
sound.set_volume(0.1)
sound2 = mixer.Sound('musics/12.wav')
sound2.set_volume(0.1)
image = cv2.imread("black_pixel.png")
image = cv2.resize(image, (100,100))
cv2.imshow('Hi !',image)
while 1 :
    if cv2.waitKey(1) & 0xFF == ord('q'):
        mixer.quit()
        break
    elif cv2.waitKey(1) & 0xFF == ord('a'):
        mixer.pause()
    elif cv2.waitKey(1) & 0xFF == ord('z'):
        mixer.unpause()
    elif cv2.waitKey(1) & 0xFF == ord('e'):
        sound.set_volume((sound.get_volume() + 0.1) % 0.5)
    elif cv2.waitKey(1) & 0xFF == ord('r'):
        sound.stop()
    elif cv2.waitKey(1) & 0xFF == ord('t'):
        sound2.stop()
    elif cv2.waitKey(1) & 0xFF == ord('y'):
        sound.play()
    elif cv2.waitKey(1) & 0xFF == ord('u'):
        sound2.play()