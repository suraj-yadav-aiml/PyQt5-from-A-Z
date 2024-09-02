import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(500, 500)
        
        self.ledTitle = QLineEdit(self.windowTitle(),self)
        self.ledTitle.move(50,50)

        self.ledTitle.setPlaceholderText("Enter the New Dialog title")
        self.ledTitle.setEchoMode(QLineEdit.Password)
        self.ledTitle.setAlignment(Qt.AlignCenter) # Qt.AlignRight
        
        self.ledTitle.textChanged.connect(self.evt_ledTitle_textChanged)

        self.btnDisable = QPushButton("Disable Edit",self)
        self.btnDisable.move(50,80)
        self.btnDisable.clicked.connect(self.evt_btnDisable_clicked)
    
    def evt_ledTitle_textChanged(self, text):
        self.setWindowTitle(text)
    
    def evt_btnDisable_clicked(self):
        if not self.ledTitle.isReadOnly():
            self.ledTitle.setReadOnly(True)
            self.btnDisable.setText("Enable Edit")
        else:
            self.ledTitle.setReadOnly(False)
            self.btnDisable.setText("Disable Edit")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
