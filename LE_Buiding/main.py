from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtCore import QSize
# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

    # Override method
    def resizeEvent(self, event: QResizeEvent) -> None:
        old_size = event.oldSize()
        new_size = QSize(self.geometry().width(), self.geometry().height())
        print(f"old_size: {old_size}, new_size: {new_size}")
        QMainWindow.resizeEvent(self, event)

def main():
    app = QApplication(sys.argv)
    wi``````ndow = MainW``````indow()
    window.setWindowTitle("LE Building")
    window.show() 
    app.exec()

if __name__ == '__main__':
    main()
