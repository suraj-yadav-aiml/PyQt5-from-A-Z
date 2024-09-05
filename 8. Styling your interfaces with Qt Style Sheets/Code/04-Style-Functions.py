import sys
from PyQt5.QtWidgets import *
from styles_macos import styleDeleteButton,styleSaveButton,styleRadioButtons
# from styles_finished import styleDeleteButton,styleSaveButton,styleRadioButtons


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.btnAdd1 = QPushButton("Add Button 1")
        self.btnAdd2 = QPushButton("Add Button 2")
        self.btnAdd1.setStyleSheet(styleSaveButton())
        self.btnAdd2.setStyleSheet(styleSaveButton())

        self.btnDel1 = QPushButton("Delete Button 1")
        self.btnDel2 = QPushButton("Delete Button 2")
        self.btnDel1.setStyleSheet(styleDeleteButton())
        self.btnDel2.setStyleSheet(styleDeleteButton())

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.btnAdd1)
        self.lytMain.addWidget(self.btnAdd2)
        self.lytMain.addWidget(self.btnDel1)
        self.lytMain.addWidget(self.btnDel2)

        self.setLayout(self.lytMain)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())