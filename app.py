from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


# Signals & slots
## Signals are notifications emitted by widgets when something happens. E.g. pressing a button, changing input text, etc.
## Slots is the name Qt uses for the receiver of signals. Any function can be used as a slot -- simply by connecting the signal to it.

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Python Text To Speech")
        # create button widget
        button = QPushButton('Click Me!')
        # provide a toggle state for button; False by default
        button.setCheckable(True)
        # exploring the 'clicked' signal
        ## use .connect to connect a function to a signal
        button.clicked.connect(self.on_click)
        button.clicked.connect(self.on_toggle)
        self.setCentralWidget(button)
        self.c = 1

    # slot for clicking signal (from .clicked)
    def on_click(self):
        print('Clicked!', self.c)
        self.c += 1
    
    # slot for toggle signal (from .clicked)
    def on_toggle(self, checked):
        print('Checked?', checked)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()