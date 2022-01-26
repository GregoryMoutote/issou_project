import threading

class RefreshThread(threading.Thread):
    def __init__(self, interface):
        threading.Thread.__init__(self)
        self.interface = interface
        self.go_on = True
        pass

    def run(self):
        while self.go_on :
            self.interface.show_hand()
        pass


    def end_refresh(self):
        self.go_on = False
        pass