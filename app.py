# import statements
from PyQt5.QtCore import QEvent, QObject, QSize, QThread, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit
import sys
from gtts import gTTS
from playsound import playsound
from platform import platform


# Worker class for the thread
class Worker(QObject):
    # create a signal that will be emitted when the thread is finished
    finished = pyqtSignal()

    # create welcome message function that will be called in the thread
    def welcome_message(self):
        # play welcome message
        playsound('welcome.mp3')
        # emit the finished signal
        self.finished.emit()

#  Suubclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    # When you subclass a Qt class you must always call the super __init__ function to allow Qt to set up the object.
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        # install event filter to allow the thread to be started when the window is shown
        self.installEventFilter(self)
        # instantiate the counter variable
        self.counter = 0

        # set the window title and minimum size
        self.setWindowTitle('Python Text To Speech')
        self.setMinimumSize(QSize(500, 500))

        # create title label
        self.title = QLabel('Welcome To Python Text To Speech')
        # customise the title label
        titleFont = self.title.font()
        titleFont.setPointSize(20)
        self.title.setFont(titleFont)
        # set the alignment of the title label
        self.title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)


        # create image label
        self.image_label = QLabel(self)
        # create image pixmap
        self.image = QPixmap('logo.png')
        # set the image label to the image pixmap
        self.image_label.setPixmap(self.image)

        # create text label
        self.text_label = QLabel('This Application is used to convert text to speech. This proves useful for people who are blind to be able to read text to promote learning thus satisfying the second AU Goal which states: "Well educated citizens and skills revolution underpinned by Science, Technology and Innovation."', self)
        # set word wrap to true
        self.text_label.setWordWrap(True)
        # customise the text label
        text_label_font = self.text_label.font()
        text_label_font.setPointSize(12)
        self.text_label.setFont(text_label_font)
        # set minimum size of the text label to image size for proper alignment
        self.text_label.setMinimumHeight(self.image.height())
        # add custom style sheet to the text label
        self.text_label.setStyleSheet('''
        padding: 0px 10px 0px 10px;
        ''')

        # create text field
        self.text_input = QTextEdit()
        # set placeholder text
        self.text_input.setPlaceholderText('Enter text here')
        # set fotn size of the text field
        self.text_input.setFontPointSize(12)

        # create convert input button
        self.convert_input_button = QPushButton('Convert Text To Speech')
        # set checkable to true to allow the button to be checked and emit a signal when clicked
        self.convert_input_button.setCheckable(True)
        # connect the clicked signal to the on_input_button_click function
        self.convert_input_button.clicked.connect(self.on_input_button_click)


        # create layout
        layout = QVBoxLayout()
        H_layout = QHBoxLayout()

        # add widgets to H_layout
        H_layout.setAlignment(Qt.AlignCenter)
        H_layout.addWidget(self.image_label)
        H_layout.addWidget(self.text_label)

        # add widgets and H_layout to the layout
        layout.addWidget(self.title)
        layout.addLayout(H_layout)
        layout.addWidget(self.text_input, 1)
        layout.addWidget(self.convert_input_button)
        

        # create a container widget and set the layout to the layout variable
        container = QWidget()
        container.setLayout(layout)

        # set central widget of the window to the container widget
        self.setCentralWidget(container)


    # create an event filter to allow the thread to be started when the window is shown
    def eventFilter(self, obj, event):
        # check if the ecvent is the window show event and the counter is 0
        if (event.type() == QEvent.Show and self.counter == 0):
            # check if the platform is windows or linux to determine how to initialise the thread
            if 'linux' in platform().lower():
                self.thread = QThread(parent=self)
                self.worker = Worker(parent=self)
            else:
                self.thread = QThread()
                self.worker = Worker()
            
            # move the worker to the thread
            self.worker.moveToThread(self.thread)
            # connect the started signal to the welcome_message function
            self.thread.started.connect(self.worker.welcome_message)
            # connect the fiinised signal to self.thread.quit() to stop the thread
            self.worker.finished.connect(self.thread.quit)
            # terminate the thread when the window is closed
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            # start the thread
            self.thread.start()
            # increment the counter
            self.counter += 1
            return True
        return super(MainWindow, self).eventFilter(obj, event)


    # This function is called when the convert_input_button is clicked
    def on_input_button_click(self):
        # get the text from the text_input
        self.text = self.text_input.toPlainText()
        # convert the text to speech using Google Text To Speech API
        tts = gTTS(text=self.text, lang='en')
        # save the audio file
        tts.save('output.mp3')
        # play the audio file
        playsound('output.mp3') 


# main function that is called when the program is run
def main():
    # create an instance of the application
    # sys.argv is the list of command line arguments passed to the Python script
    app = QApplication(sys.argv)
    # create an instance of the main window
    window = MainWindow()
    # show the main window since it is hidden by default``
    window.show()
    # start the event loop
    sys.exit(app.exec_())


# run the main function
if __name__ == '__main__':
    main()
