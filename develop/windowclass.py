from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Window")
        self.setWindowIcon(QIcon("qt.png"))
        #self.setFixedHeight(200)
        #self.setFixedWidth(200)

        self.setGeometry(400,300,800,500)
        #self.setStyleSheet('background-color:red')

        stylesheet = (
            'background-color:silver'
        )

        self.setStyleSheet(stylesheet)



app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())