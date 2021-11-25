from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from gtts import gTTS
from playsound import playsound


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.checked = True
        self.setWindowTitle("Python Text To Speech")
        self.button = QPushButton('Click Me!')
        self.setCentralWidget(self.button)
        self.button.setCheckable(True)
        self.button.setChecked(self.checked)
        self.button.clicked.connect(self.on_toggle)

    def on_toggle(self):
        self.tts = gTTS(text='clicked!', lang="en")
        self.tts.save("output.mp3")
        playsound('output.mp3')
        
        
        



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()