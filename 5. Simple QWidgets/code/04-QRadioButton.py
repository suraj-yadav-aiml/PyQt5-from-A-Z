import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.lbl = QLabel("My Label",self)
        self.lbl.setStyleSheet("color:red")
        self.lbl.move(50,30)
        

        self.rbtRed = QRadioButton("Red",self)
        self.rbtRed.move(50,50)
        self.rbtRed.setChecked(True)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)

        self.rbtBlue = QRadioButton("Blue",self)
        self.rbtBlue.move(50,70)
        self.rbtBlue.clicked.connect(self.evt_rbt_clicked)

        self.rbtGreen = QRadioButton("Green",self)
        self.rbtGreen.move(50,90)
        self.rbtGreen.clicked.connect(self.evt_rbt_clicked)
    
    def evt_rbt_clicked(self):
        rbt = self.sender()
        rbt_color = rbt.text()
        self.lbl.setStyleSheet(f"color:{rbt_color}")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
