from PyQt6.QtWidgets import QWidget
from Config import Config

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('LE Building')

        self.window_width = int(self.config.read_setting_data("screen_width"))
        self.height = int(self.config.read_setting_data("screen_height"))

        # TODO: center the spawning position of the window
        self.setGeometry(0, 0, self.window_width, self.height)
    
    def resizeEvent(self, event):
        screen = event.size()
        self.width = screen.width()
        self.height = screen.height()
        print("w: " + str(self.width) + " h: " + str(self.height) )

    def closeEvent(self,event) -> None:
        self.get_all_value_to_config()
        self.config.save_file()

    def get_all_value_to_config(self) -> None:
        self.config.write_setting_data("screen_width", str(self.width))
        self.config.write_setting_data("screen_height", str(self.height))
