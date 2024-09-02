import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)
        
        self.ledTitle = QLineEdit(self.windowTitle(),self)
        self.ledTitle.move(50,50)

        self.ledTitle.textChanged.connect(self.evt_ledTitle_textChanged)
    
    def evt_ledTitle_textChanged(self, text):
        self.setWindowTitle(text)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
