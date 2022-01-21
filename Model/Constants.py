import ctypes

class Constants:
    screen = ctypes.windll.user32
    TARGET_RADIUS = 0.035 * screen.GetSystemMetrics(0)