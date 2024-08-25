import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500, 500)

        self.btn = QPushButton("Show Text Input", self)
        self.btn.move(40, 20)
        self.btn.clicked.connect(self.evt_btn_clicked_getText)

        self.btn = QPushButton("Show Int Input", self)
        self.btn.move(40, 60)
        self.btn.clicked.connect(self.evt_btn_clicked_getInt)

        self.btn = QPushButton("Show Double Input", self)
        self.btn.move(40, 100)
        self.btn.clicked.connect(self.evt_btn_clicked_getDouble)

        self.btn = QPushButton("Show Dropdown Input", self)
        self.btn.move(40, 140)
        self.btn.clicked.connect(self.evt_btn_clicked_getItem)

    def evt_btn_clicked_getText(self):
        sName, bOK = QInputDialog.getText(self,"Text","Enter your name : ")
        if bOK:
            QMessageBox.information(self,"Name",f"Your name is : {sName}")
        else:
            QMessageBox.critical(self,"Cancelled","User Cancelled")


    def evt_btn_clicked_getInt(self):
        iAge, bOK = QInputDialog.getInt(self,"Age","Enter your age : ", 18, 18, 80, 1) # default,min,max,step
        if bOK:
            QMessageBox.information(self,"Coffee",f"Your age is : {iAge}")
        else:
            QMessageBox.critical(self,"Cancelled","User Cancelled")    

    
    def evt_btn_clicked_getDouble(self):
        dCost, bOK = QInputDialog.getDouble(self,"Coffee","Enter the cost of your coffee : ", 120.0, 160.0, 500.0, 1) # default,min,max,step
        if bOK:
            QMessageBox.information(self,"Age",f"Your cost was : {dCost}")
        else:
            QMessageBox.critical(self,"Cancelled","User Cancelled")  


    def evt_btn_clicked_getItem(self):
        lstColor = ["Red", "Green", "Blue"]
        sColor, bOk = QInputDialog.getItem(self, "Text", "Enter your favorite color: ", lstColor, editable=False)
        if bOk:
            QMessageBox.information(self, "Name", "Your favorite color is "+sColor)
        else:
            QMessageBox.critical(self, "Canceled", "User canceled")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
