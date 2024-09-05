import sys
from PyQt5.QtWidgets import *
import qdarkstyle
import styles_finished as qss

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Come on over to the darkstyle")

        self.lytMain = QHBoxLayout()
        self.setLayout(self.lytMain)

        self.gbxDarkStyle = QGroupBox("Dark Style")
        self.gbxDarkStyle.setCheckable(True)
        self.lytMain.addWidget(self.gbxDarkStyle)

        self.lytGbx = QHBoxLayout()
        self.gbxDarkStyle.setLayout(self.lytGbx)

        self.rbtnNormal = QRadioButton("Normal")
        self.rbtnNormal.setCheckable(True)
        self.rbtnDark = QRadioButton("Dark")

        self.lytBtn = QVBoxLayout()
        self.lytBtn.addWidget(self.rbtnNormal)
        self.lytBtn.addWidget(self.rbtnDark)
        self.lytGbx.addLayout(self.lytBtn)

        self.ptedt = QPlainTextEdit()
        self.lytGbx.addWidget(self.ptedt)
        

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())