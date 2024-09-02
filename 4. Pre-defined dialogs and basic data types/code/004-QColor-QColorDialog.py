import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("Choose Color", self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.evt_btn_clicked)

    # def evt_btn_clicked(self):
    #     color = QColorDialog.getColor(QColor("#FF0000"), self, "Choose Color")
    #     print(color)

    def evt_btn_clicked(self):
        color = QColorDialog.getColor(QColor("cornsilk"), self, "Choose Color")
        print(color)
        print(color.getRgb()) # (255, 248, 220, 255)
        print(color.name())  # #fff8dc
        print(color.getHsl())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
