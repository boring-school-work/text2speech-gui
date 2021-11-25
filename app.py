from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
import sys
from gtts import gTTS
from playsound import playsound


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Python Text To Speech')
        self.setMinimumSize(QSize(500, 500))

        self.button = QPushButton('Print')
        self.label = QLabel()
        self.input = QLineEdit()
        self.button.setCheckable(True)
        self.button.clicked.connect(self.on_click)
        # self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def on_click(self):
        self.text = self.input.text()
        tts = gTTS(text=self.text, lang='en')
        tts.save('output.mp3')
        self.label.setText(self.text)
        playsound('output.mp3')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()