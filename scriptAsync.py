import multiprocessing

import keyboard


def worker():
    """worker function"""
    while 1:
        print ('Worker')
        if keyboard.is_pressed("q"):
            break
    return

if __name__ == '__main__':
    class
    p = multiprocessing.Process(target=worker)
    p.start()
    while 1 :
        print("cc les bgs")
        if keyboard.is_pressed("q"):
            print("j'ai appuye sur Q")
            p.join()
            break
