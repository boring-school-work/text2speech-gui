from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


# Suubclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    # When you subclass a Qt class you must always call the super __init__ function to allow Qt to set up the object.
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Python Text To Speech")
        button = QPushButton("Click Me")
        # # As well as .setFixedSize() 
        self.setFixedSize(QSize(500, 500))

        # # .setMinimumSize() to set the minimum size of the window
        self.setMinimumSize(QSize(500, 500))

        # .setMaximumSize() sets the maximum size of the window.
        self.setMaximumSize(QSize(500, 500))

        # set central widget
        self.setCentralWidget(button)



app = QApplication(sys.argv)

window = MainWindow()
window.show()


# start the event loop
app.exec_()