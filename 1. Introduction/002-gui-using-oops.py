import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui with OOPs")
        self.resize(500,500)

        self.ledText = QLineEdit("My Gui",self)
        self.ledText.move(20,50)

        self.btnUpdate = QPushButton("Update Window Title",self)
        self.btnUpdate.move(20,80)
        self.btnUpdate.clicked.connect(self.evt_btnUpdate_clicked)
    
    def evt_btnUpdate_clicked(self):
        self.setWindowTitle(self.ledText.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)    # Create Application
    dlgMain = DlgMain()             # Main GUI Canvas
    dlgMain.show()                  # Show GUI

    sys.exit(app.exec_())