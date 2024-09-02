import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500,500)

        self.spbInt = QSpinBox(self)
        self.spbInt.move(50,10)
        self.spbInt.setWrapping(True) # Kind of start again after max value it start from beggining
        self.spbInt.setRange(0,1000)
        self.spbInt.setSingleStep(100)
        self.spbInt.setValue(300)
        self.spbInt.valueChanged.connect(self.evt_spbInt_valueChnaged)

        self.spbDbl = QDoubleSpinBox(self)
        self.spbDbl.move(50,80)
        self.spbDbl.setDecimals(5)
        self.spbDbl.setSingleStep(0.01)
        self.spbDbl.setPrefix("Latitude: ")
        self.spbDbl.setSuffix(chr(176))
        self.spbDbl.setRange(-90,90)
        self.spbDbl.valueChanged.connect(self.evt_spbDbl_valueChanged)
        self.spbInt.editingFinished.connect(self.evt_spbInt_editingFinished)

        self.lbl_warning = QLabel("",self)
        self.lbl_warning.move(50,40)
        self.lbl_warning.resize(400,50)
        self.lbl_warning.setStyleSheet("font-size:20px;color:red")

    def evt_spbInt_valueChnaged(self, val):
        if val % 100 :
            self.spbInt.setStyleSheet("color:red")
            self.lbl_warning.setText("Value must be divisible by 100")
        else:
            self.spbInt.setStyleSheet("color:black")
            self.lbl_warning.setText("")
    
    def evt_spbInt_editingFinished(self):
        if self.spbInt.value() % 100:
            QMessageBox.critical(self,"Invalid Number","Invalid Value Entered!!!\n\nMust be divisible by 100")
            self.spbInt.setFocus()
    
    def evt_spbDbl_valueChanged(self,val):
        print(self.spbDbl.text())
        print(self.spbDbl.value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())

    # 11:23
