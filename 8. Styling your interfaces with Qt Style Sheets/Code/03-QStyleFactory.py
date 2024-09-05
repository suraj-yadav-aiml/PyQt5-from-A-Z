import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")


        self.btn_1 = QPushButton("Button 1")
        self.btn_2 = QPushButton("Button 2")
        self.btn_3 = QPushButton("Button 3")
        self.chk1 = QCheckBox("Checkbox-1")
        self.led1 = QLineEdit("Editable")
        self.led2 = QLineEdit("Read Only")
        self.led2.setReadOnly(True)

        self.lst = QListWidget()
        self.lst.addItems(QStyleFactory.keys())
        self.lst.itemDoubleClicked.connect(self.evt_lst_dbl)

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.btn_1)
        self.lytMain.addWidget(self.btn_2)
        self.lytMain.addWidget(self.btn_3)
        self.lytMain.addWidget(self.chk1)
        self.lytMain.addWidget(self.led1)
        self.lytMain.addWidget(self.led2)
        self.lytMain.addWidget(QProgressBar())
        self.lytMain.addWidget(QSlider())
        self.lytMain.addWidget(QDial())
        self.lytMain.addWidget(self.lst)

        self.setLayout(self.lytMain)

    def evt_lst_dbl(self, itm):
        app.setStyle(QStyleFactory.create(itm.text()))
        # QMessageBox.information(self,"Set Style",f"You selected the '{itm.text()}' style")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
