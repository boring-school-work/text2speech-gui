from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit
import sys
from gtts import gTTS
from playsound import playsound


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Python Text To Speech')
        self.setMinimumSize(QSize(500, 500))

        self.button = QPushButton('Convert Text To Speech')
        self.button.clicked.connect(self.on_click)
        self.button.setCheckable(True)
        self.button.setMinimumSize(QSize(600, 35))

        self.input = QTextEdit()
        self.input.setMinimumSize(QSize(600, 600))
        self.input.setPlaceholderText('Enter text here')

        self.title = QLabel('Welcome To Python Text To Speech')
        titleFont = self.title.font()
        titleFont.setPointSize(20)
        self.title.setFont(titleFont)
        self.title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.label = QLabel(self)
        self.image = QPixmap('logo.png')
        self.label.setPixmap(self.image)

        self.text_label = QLabel('This Application is used to convert text to speech. This proves useful for people who are blind to be able to read text to promote learning thus satifying the second AU Goal which states: "Well educated citizens and skills revolution underpinned by Science, Technology and Innovation."', self)
        self.text_label.setWordWrap(True)
        labelFont = self.text_label.font()
        labelFont.setPointSize(12)
        self.text_label.setFont(labelFont)
        self.text_label.setMinimumHeight(self.image.height())
        self.text_label.setStyleSheet('''
        padding: 0px 10px 0px 10px;
        ''')


        V_layout = QVBoxLayout()
        H_layout = QHBoxLayout()

        H_layout.setAlignment(Qt.AlignCenter)

        H_layout.addWidget(self.label)
        H_layout.addWidget(self.text_label)        

        V_layout.addWidget(self.title)
        V_layout.addLayout(H_layout)
        V_layout.addWidget(self.input)
        V_layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(V_layout)

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