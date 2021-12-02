from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QTextEdit
import sys
from gtts import gTTS
from playsound import playsound


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Python Text To Speech')
        self.setMinimumSize(QSize(500, 500))

        self.setMouseTracking(True)

        self.label = QLabel('Click in this window')
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText('mouseMoveEvent')

    def mousePressEvent(self, e):
        self.label.setText('mousePressEvent')
    
    def mouseReleaseEvent(self, e):
        self.label.setText('mouseReleaseEvent')
    
    def mouseDoubleClickEvent(self, e):
        self.label.setText('mouseDoubleClickEvent')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()