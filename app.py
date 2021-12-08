from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit
import sys
from gtts import gTTS
from playsound import playsound


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Python Text To Speech')
        self.setMinimumSize(QSize(500, 500))

        self.title = QLabel('Welcome To Python Text To Speech')
        titleFont = self.title.font()
        titleFont.setPointSize(20)
        self.title.setFont(titleFont)
        self.title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.image_label = QLabel(self)
        self.image = QPixmap('logo.png')
        self.image_label.setPixmap(self.image)

        self.text_label = QLabel('This Application is used to convert text to speech. This proves useful for people who are blind to be able to read text to promote learning thus satifying the second AU Goal which states: "Well educated citizens and skills revolution underpinned by Science, Technology and Innovation."', self)
        self.text_label.setWordWrap(True)
        text_label_font = self.text_label.font()
        text_label_font.setPointSize(12)
        self.text_label.setFont(text_label_font)
        self.text_label.setMinimumHeight(self.image.height())
        self.text_label.setStyleSheet('''
        padding: 0px 10px 0px 10px;
        ''')

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText('Enter text here')
        self.text_input.setFontPointSize(12)

        self.convert_input_button = QPushButton('Convert Text To Speech')
        self.convert_input_button.setCheckable(True)
        self.convert_input_button.clicked.connect(self.on_input_button_click)

        layout = QVBoxLayout()
        H_layout = QHBoxLayout()

        H_layout.setAlignment(Qt.AlignCenter)
        H_layout.addWidget(self.image_label)
        H_layout.addWidget(self.text_label)

        layout.addWidget(self.title)
        layout.addLayout(H_layout)
        layout.addWidget(self.text_input, 1)
        layout.addWidget(self.convert_input_button)
        

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


    def on_input_button_click(self):
        self.text = self.text_input.toPlainText()
        tts = gTTS(text=self.text, lang='en')
        tts.save('output.mp3')
        playsound('output.mp3') 


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()