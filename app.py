from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.button_checked = True
        self.setWindowTitle("Python Text To Speech")
        self.button = QPushButton('Click Me!')

        # if a widget does not provide a signal that sends the current state, you need to retrive the value from the widget directly in your handler
        self.button.setCheckable(True)
        self.button.released.connect(self.on_release)
        self.button.setChecked(self.button_checked)
        self.setCentralWidget(self.button)
    
    def on_release(self):
        print(self.button.isChecked())
        self.button_checked = self.button.isChecked()
        print(self.button_checked)
        
        



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()