from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QFileDialog, QMessageBox
import sys
from gtts import gTTS
from playsound import playsound
import docx2txt
from pdf2docx import parse


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
        self.text_input.setMaximumSize(QSize(960, 765))
        self.text_input.setPlaceholderText('Enter text here')

        self.convert_input_button = QPushButton('Convert Text To Speech')
        self.convert_input_button.setCheckable(True)
        self.convert_input_button.clicked.connect(self.on_input_button_click)
        self.convert_input_button.setMaximumSize(QSize(960, 35))

        self.file_label = QLabel("Select file to convert to speech")
        file_label_font = self.file_label.font()
        file_label_font.setPointSize(15)
        self.file_label.setFont(file_label_font)

        self.choose_file_button = QPushButton("Select file")
        self.choose_file_button.setCheckable(True)
        self.choose_file_button.clicked.connect(self.openFileNameDialog)
        self.choose_file_button.setFixedSize(QSize(100, 35))

        self.file_label_data = QLabel("")
        file_label_data_font = self.file_label_data.font()
        file_label_data_font.setPointSize(12)
        self.file_label_data.setFont(file_label_data_font)

        self.play_button = QPushButton("Play")
        self.play_button.setCheckable(True)
        self.play_button.setFixedSize(QSize(100, 35))
        self.play_button.clicked.connect(self.play_audio)

        layout = QVBoxLayout()
        V_layout_1 = QVBoxLayout()
        H_layout_1 = QHBoxLayout()
        H_layout_2 = QHBoxLayout()
        self.grid = QGridLayout()

        H_layout_1.setAlignment(Qt.AlignCenter)
        H_layout_1.addWidget(self.image_label)
        H_layout_1.addWidget(self.text_label)

        V_layout_1.addWidget(self.text_input, 1)
        V_layout_1.addWidget(self.convert_input_button)

        self.grid.addWidget(self.file_label, 0, 0, 1, 2, Qt.AlignCenter)
        self.grid.addWidget(self.choose_file_button, 1, 0, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.play_button, 1, 1, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.file_label_data, 2, 0, 1, 2, Qt.AlignCenter)

        H_layout_2.addLayout(V_layout_1)
        H_layout_2.addLayout(self.grid)
     
        layout.addWidget(self.title)
        layout.addLayout(H_layout_1)
        layout.addLayout(H_layout_2)
        

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


    def on_input_button_click(self):
        self.text = self.text_input.toPlainText()
        tts = gTTS(text=self.text, lang='en')
        tts.save('output.mp3')
        playsound('output.mp3')


    def convert_docx_to_speech(self, file_name):
        tts = gTTS(text=docx2txt.process(file_name), lang='en')
        tts.save(file_name.replace('.docx', '.mp3'))


    def convert_pdf_to_speech(self, file_name):
        doc_file_path = file_name.replace('.pdf', '.docx')
        parse(file_name, doc_file_path)
        tts = gTTS(text=docx2txt.process(doc_file_path), lang='en')
        tts.save(file_name.replace('.pdf', '.mp3'))


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Word Document (*.doc);;Pdf Document (*.pdf)", options=options)
        if self.fileName:
            if self.fileName.endswith('.docx'):
                self.file_label_data.setText(f'Converting {self.fileName} to speech...')
                self.convert_docx_to_speech(self.fileName)
                self.file_label_data.setText(f'Converted {self.fileName} to speech\nYou can play the audio file by clicking on play button')
            elif self.fileName.endswith('.pdf'):
                self.file_label_data.setText(f'Converting {self.fileName} to speech...')
                self.convert_pdf_to_speech(self.fileName)
                self.file_label_data.setText(f'Converted {self.fileName} to speech\nYou can play the audio file by clicking on play button')

    def play_audio(self):
        if self.fileName.endswith('.docx'):
            playsound(self.fileName.replace('.docx', '.mp3'))
        elif self.fileName.endswith('.pdf'):
            playsound(self.fileName.replace('.pdf', '.mp3'))       




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()