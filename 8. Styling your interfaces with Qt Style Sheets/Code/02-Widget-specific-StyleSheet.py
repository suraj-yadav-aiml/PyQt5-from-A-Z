import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        sStyle = """
            QPushButton {
                background-color:red; 
                border-radius:5px; 
                padding:8px;
                margin: 10px
            }

            QPushButton:default {
                background-color:blue;
                color: white; 
                border-radius:5px; 
                padding:3px
            }

            QPushButton:default:hover {
                background-color:white;
                color: black; 
                border-radius:5px; 
                padding:3px
            }

            QPushButton:hover {
                background-color:green;
                color: white; 
                border-radius:5px; 
                border: 3px solid #000000;
                padding:3px
            }

            QCheckBox {
                background-color: peru;
                color: cornsilk;
                padding: 5px;
                border-radius: 5px;
            }

            QCheckBox:checked {
                background-color: cornsilk;
                color: peru;
                padding: 5px;
                border-radius: 5px;
            }

            QCheckBox::indicator {
                background-color: purple;
                color: peru;
                padding: 5px;
                border-radius: 5px;
            }

            QCheckBox::indicator:checked {
                background-color: green;
                color: peru;
                padding: 5px;
                border-radius: 5px;
            }

            QLineEdit:read-only {
                color: #777777;
                font-style: italic;
            }

        """

        self.setStyleSheet(sStyle)

        self.btn_1 = QPushButton("Button 1")
        self.btn_2 = QPushButton("Button 2")
        self.btn_3 = QPushButton("Button 3")
        self.chk1 = QCheckBox("Checkbox-1")
        self.led1 = QLineEdit("Editable")
        self.led2 = QLineEdit("Read Only")
        self.led2.setReadOnly(True)

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.btn_1)
        self.lytMain.addWidget(self.btn_2)
        self.lytMain.addWidget(self.btn_3)
        self.lytMain.addWidget(self.chk1)
        self.lytMain.addWidget(self.led1)
        self.lytMain.addWidget(self.led2)

        self.setLayout(self.lytMain)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
