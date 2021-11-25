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

        self.button = QPushButton('Convert Text To Speech')
        self.input = QTextEdit()
        self.input.setFixedSize(QSize(500, 500))
        self.input.setPlaceholderText('Enter text here')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def on_click(self):
        self.text = self.input.toPlainText()
        tts = gTTS(text=self.text, lang='en')
        tts.save('output.mp3')
        playsound('output.mp3')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()