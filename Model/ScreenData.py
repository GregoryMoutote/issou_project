import platform

class ScreenData:
    def __init__(self):
        if platform.system() == 'Windows':
            import ctypes
            screen = ctypes.windll.user32
            self.width = screen.GetSystemMetrics(0)
            self.height = screen.GetSystemMetrics(1)
        elif platform.system() == 'Linux':
            from screeninfo import get_monitors
            
            for monitor in get_monitors():
                self.width = monitor.width
                self.height = monitor.height


        else:
            self.width = 1920
            self.height = 1080
