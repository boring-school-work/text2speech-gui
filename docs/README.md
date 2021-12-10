# Technical Documentation
## 🤔 Problem Statement
Create a text to speech application in python.

## 🎯 Scope
Criteria | Description
----- | -----
**Must have** | Convert text to speech; User interface
**Nice to have** | Welcome messages
**Not in scope** | Convert text in a file to speech (Worked in linux but debbugging will take time for this feature to be compatible in windows)

## 🚩 Milestones and deadlines
Milestone | Deadline | Status
----- | ----- | -----
Working on converting text input to speech | Nov 21, 2021 | Completed
Build a user interface | Nov 22, 2021 | Completed
Test features | Nov 25, 2021 | Completed
Working on user interface | Dec 6, 2021 | Completed
Working on adding and converting files on converting text input to speech | Dec 8, 2021 | Completed
Research on additional data | Dec 10, 2021 | Completed

## Reference materials
* [PyQt5 Tutorial 2021, Create Python GUIs with Qt ](https://www.pythonguis.com/pyqt5-tutorial/)
* [Qt for Python — Qt for Python](https://doc.qt.io/qtforpython-5/) 
* [Use PyQt's QThread to Prevent Freezing GUIs – Real Python](https://realpython.com/python-pyqt-qthread/#worker-threads)


## Explaining The Code

> 📝 Worth noting: All modules inside PyQt5 are classes.

#### Imports
```{.py, .numberLines}
from PyQt5.QtCore import QEvent, QObject, QSize, QThread, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit
import sys
from gtts import gTTS
from playsound import playsound
from platform import platform
```
* `QSize` : It defines the size of a two-dimensional object using integer point precision.
* `Qt` : It is a namespace that contains miscellaneous identifiers used throughout the Qt library. These include alignments, cursor, gestures, etc. 
* `QPixmap` : It is an off-screen image representation that can be used as a paint device. 
* `QApplication` : This class manages the GUI application’s control flow and main settings
* `QHBoxLayout` : This class lines up widgets horizontally.
* `QLabel` : This class provides a text or image display widget.
* `QVBoxLayout` : This class lines up widgets vertically.
* `QWidget` : It is the base class of all user interface objects.
* `QPushButton` : This widget provides a command button. 
* `QTextEdit` : It is a class that provides a widget that is used to edit and display both plain and rich text. 
* `QMainWindow` : This class provides a main application window. 
* `sys` : This module provides variables that are used or maintained by the interpreter.
* `playsound` : A python module that plays sound.
* `gtts` : Google text to speech library to interface Google’s text-to-speech API.
* `QEvent` : It is the base class of all event classes.
* `QObject` : It is the base class of all Qt objects. 
* `QThread` : This class provides a platform-independent way to manage threads.
* `pyqtSignal` : It is a class allows the definition of a custom signal in PyQt5 
* `platform` :  This module is used to retrieve platform-identifying data


> QApplication, QHBoxLayout, QLabel, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit are all widgets in the Qt library.


#### Code Body
```python3
class Worker(QObject):
    finished = pyqtSignal()

    def welcome_message(self):
        playsound('welcome.mp3')
        self.finished.emit()
```
* This `Worker` class is a worker thread for the PyQt5 application. 

> Worker threads are secondary threads of execution that can be used to offload long-running tasks from the main thread and prevent GUI from freezing.

* This worker thread is necessary because we decided to add a welcome message when the app first loads. It allows the welcome message to play without interrupting the running of the GUI part of the application. 
* It takes a `QObject` arguement to inherit the properties of objects in PyQt5.
* It has `welcome_message` function which runs when the thread starts.
* `finished` is a custom signal that is created by using `pyqtSignal` class.
* **From line 6**, the signal is emitted to show that the process is done.


```python3
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
```
* It is useful to subclass (convert into a class) `QMainWindow` to allow the easy customization of the application’s main window.
* Whenever a Qt class is ‘subclassed’, you must always call the `super().__init__()` function to allow Qt to set up the object. 


```python3
self.installEventFilter(self)
self.counter = 0
```
* `installEventFilter()` function enables the interception of events delivered by objects. 
* The `eventFilter()` function later defined in the code handles a specified event that is intercepted.
* `self.counter` variable counts the number of time the window is opened.


```python3
self.setWindowTitle('Python Text To Speech')
self.setMinimumSize(QSize(500, 500))
```
* **Line 1** sets the window title.
* **Line 2** sets the minimum size of the window when the code is executed.


```python3
self.title = QLabel('Welcome To Python Text To Speech')
titleFont = self.title.font()
titleFont.setPointSize(20)
self.title.setFont(titleFont)
self.title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
```
* `self.title` is a varible that contains a `QLabel` widget that contains a string value that sets its text.
* The `titleFont` variable is the return value of `QLabel.font()` which allows the manipulation of font properties of `self.title`.
* `.setPointSize(int)` sets the font size of the text.
* `.setFont()` attributes takes the value of `titleFont` and applies the changes to the `self.title` *QLabel*.
* `.setAlignment()` is used to define the alignment properties of `self.title`.
* `Qt.AlignTop` aligns the widget to the top of its available space. 
* `Qt.AlignHCenter` aligns the widget to be centered-horizontally in the available space for the widget.


```python3
self.image_label = QLabel(self)
self.image = QPixmap('logo.png')
self.image_label.setPixmap(self.image)
```
* `self.image_label` is also a *QLabel* object.
* `self.image` is set with `QPixmap()` because it sets an off-screen image representation in PyQt5.
* `.setPixmap()` takes `self.image` as a value to set `self.image_label` as an image.


```python3
self.text_label = QLabel('This Application is used to convert text to speech. This proves useful for people who are blind to be able to read text to promote learning thus satisfying the second AU Goal which states: "Well educated citizens and skills revolution underpinned by Science, Technology and Innovation."', self)
self.text_label.setWordWrap(True)
text_label_font = self.text_label.font()
text_label_font.setPointSize(12)
self.text_label.setFont(text_label_font)
self.text_label.setMinimumHeight(self.image.height())
self.text_label.setStyleSheet('''
padding: 0px 10px 0px 10px;
''')
```
* `self.text_label` is a *QLabel* object with a string as an arguement.
* `.setWordWrap(True)` method is used to allow wrapping of text on the screen as the window size changes.
* Just as in `self.title`, the `.font()` method allows the manipulation of font properties.
* `.setMinimumHeight()` sets the minimum height of the QLabel object. This is set to the image height to allow `self.text_label` to perfectly align `self.image_label`. 
* `.setStyleSheet()` method allows the addition of styling properties to the QLabel object. It takes css code as a parameter.


```python3
self.text_input = QTextEdit()
self.text_input.setPlaceholderText('Enter text here')
self.text_input.setFontPointSize(12)
```
* `self.text_input` is an object of `QTextEdit` which takes input from the user. 
* `.setPlaceholderText()` method allows the setting of placeholder text on the text area.
* `.setFontPointSize(int)` takes an integer which sets the font size of the text entered in the text area.


```python3 
self.convert_input_button = QPushButton('Convert Text To Speech')
self.convert_input_button.setCheckable(True)
self.convert_input_button.clicked.connect(self.on_input_button_click)
```
* `self.convert_input_button` creates a button object from `QPushButton`. It has the parameter of a string which sets the text displayed on the button. 
* Normal buttons in PyQt5 are always set to `False`, hence no signal is sent when the button is clicked.
* `.setCheckable(True)` makes the button have a toggle state such that it can send a signal that it has been pressed. 
* **From line 3:** `.clicked` is a signal and it is connected to a slot with `.connect`. 
* The slot for `self.convert_input_button` is `on_input_button_click`.
* This means `on_input_button_click` function runs when `self.convert_input_button` is clicked. 

> **Note:** 
> 
> Signals & slots: 
>
> Signals are notifications emitted by widgets when something happens. E.g. pressing a button, changing input text, etc. Slots is the name Qt uses for the receiver of signals. Any function can be used as a slot -- simply by connecting the signal to it.


```python3
layout = QVBoxLayout()
H_layout = QHBoxLayout()

H_layout.setAlignment(Qt.AlignCenter)
H_layout.addWidget(self.image_label)
H_layout.addWidget(self.text_label)

layout.addWidget(self.title)
layout.addLayout(H_layout)
layout.addWidget(self.text_input, 1)
layout.addWidget(self.convert_input_button)
```
* The block of code above sets the layout of the widgets in the app.
* The main layout of the application is `layout` and it is a `QVBoxLayout` object. 

> `QVBoxLayout` arranges widgets vertically.

* The two layouts used are `QVBoxLayout` and `QHBoxLayout`.

> `QHBoxLayout` arranges widgets horizontally.

* 





