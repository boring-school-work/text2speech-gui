from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


window_titles = [
    "MyApp",
    "MyApp2",
    "MyApp3",
    "MyApp4",
    "MyApp5",
    "MyApp6",
    "Something went wrong"
]


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.n_times_clicked = 0
        self.setWindowTitle(window_titles[0])
        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.on_button_clicked)
        self.setCentralWidget(self.button)
        self.windowTitleChanged.connect(self.on_window_title_changed)

    def on_button_clicked(self):
        self.n_times_clicked += 1
        new_window_title = window_titles[self.n_times_clicked]
        self.setWindowTitle(new_window_title)

    def on_window_title_changed(self, title):
        print(f"Window title changed to {title}")

        if title == 'Something went wrong':
            self.button.setDisabled(True)
        
        
        



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()