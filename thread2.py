import threading
import time

class Thread1 (threading.Thread):
    def __init__(self, jusqua):      # jusqua = donnée supplémentaire
        threading.Thread.__init__(self)  # ne pas oublier cette ligne

    def run(self):
        print("j'ai envie de mourir")
        time.sleep(3)   

