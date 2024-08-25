import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 300)

        self.btn = QPushButton("Open File: getOpenFileName", self)
        self.btn.move(40, 20)
        self.btn.clicked.connect(self.evt_btn_clicked_getOpenFileName)

        self.btn = QPushButton("Open File: getSaveFileDialog", self)
        self.btn.move(40, 60)
        self.btn.clicked.connect(self.evt_btn_clicked_getSaveFileDialog)

        self.btn = QPushButton("Open File: getOpenFileNames", self)
        self.btn.move(40, 100)
        self.btn.clicked.connect(self.evt_btn_clicked_getOpenFileNames)

    def evt_btn_clicked_getOpenFileName(self):
        res = QFileDialog.getOpenFileName(self, "Open File", "C:/Users/Admin/Downloads", "JPG File (*.jpg);;PNG Files (*.png)")
        print(res) # res is tuple containing the image path and extention -> ('C:/Users/Admin/Downloads/image.jpg', 'JPG File (*.jpg)')
                   # res would be ('', '') if user cancel the window
    
    def evt_btn_clicked_getSaveFileDialog(self): # Provide the name of the file with which you save file
        res = QFileDialog.getSaveFileName(self, "Open File", "C:/Users/Admin/Downloads", "JPG File (*.jpg);;PNG Files (*.png)")
        print(res) # ('C:/Users/Admin/Downloads/my_new_image.jpg', 'JPG File (*.jpg)')

    def evt_btn_clicked_getOpenFileNames(self):
        res = QFileDialog.getOpenFileNames(self, "Open File", "C:/Users/Admin/Downloads", "JPG File (*.jpg);;PNG Files (*.png)")
        print(res) # (['C:/Users/Admin/Downloads/image1.jpg', 'C:/Users/Admin/Downloads/image2.jpg', 'C:/Users/Admin/Downloads/image3.jpg'], 'JPG File (*.jpg)')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
