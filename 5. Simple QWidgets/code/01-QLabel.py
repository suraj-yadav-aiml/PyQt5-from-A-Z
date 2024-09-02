import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        self.btn = QPushButton("Change Label", self)
        self.btn.move(40, 40)
        self.btn.resize(120, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.lbl = QLabel("Old Text", self)
        self.lbl.move(40, 100)
        self.lbl.resize(150, 200)
        font = QFont("Times New Roman", 12, 60, True)
        self.lbl.setFont(font)

    def evt_btn_clicked(self):
        s = """
        <h1>Header</h1>
        <ul>
            <li>Red</li>
            <li>Blue</li>
        </ul>
        """
        self.lbl.setText(s)
        time.sleep(2)
        pxm = (
                QPixmap(r"D:\Suraj\LearningPath\Python GUI Projects\PyQt5 From A-Z 2020-9\5. Simple QWidgets\code\fotos\bear.jpg")
               .scaled(150,200)
               )

        if pxm.isNull():  
            QMessageBox.critical(self, "Error", "Could not load image bear.jpg")
            return 

        self.lbl.setPixmap(pxm)
        # self.lbl.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
