from os import truncate
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit
import sys
from gtts import gTTS
from playsound import playsound


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Python Text To Speech')
        self.setMinimumSize(QSize(500, 500))
        align_top_center = Qt.AlignTop | Qt.AlignHCenter

        self.button = QPushButton('Convert Text To Speech')
        self.button.clicked.connect(self.on_click)
        self.button.setCheckable(True)

        self.input = QTextEdit()
        self.input.setFixedSize(QSize(500, 500))
        self.input.setPlaceholderText('Enter text here')

        self.title = QLabel('Welcome To Python Text To Speech')
        titleFont = self.title.font()
        titleFont.setPointSize(20)
        self.title.setFont(titleFont)
        self.title.setAlignment(align_top_center)

        self.label = QLabel('This Application is used to convert text to speech. This proves useful for people who are blind to be able to read text to promote learning thus satifying the second AU Goal which states: "Well educated citizens and skills revolution underpinned by Science, Technology and Innovation."')
        self.label.setWordWrap(True)
        labelFont = self.label.font()
        labelFont.setPointSize(12)
        self.label.setFont(labelFont)
        self.label.setAlignment(align_top_center)

        self.image = QLabel()
        self.image.setPixmap(QPixmap('tts.png'))
        self.image.setAlignment(Qt.AlignTop)


        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.image)
        layout.addWidget(self.label)
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