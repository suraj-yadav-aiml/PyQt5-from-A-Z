import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(400, 200)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(10)
        self.lcd.display(99)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setStyleSheet("background-color:black;color:green")
    
        self.spbInt = QSpinBox()
        self.spbInt.setValue(125)
        self.spbInt.setRange(0,1000)
        self.spbInt.valueChanged.connect(self.evt_spbInt_valueChnaged)

        self.rbtDec = QRadioButton("Dec")
        self.rbtDec.setChecked(True)
        self.rbtHex = QRadioButton("Hex")
        self.rbtOct = QRadioButton("Oct")
        self.rbtBin = QRadioButton("Bin")
        self.lytNumSys = QHBoxLayout()
        self.lytNumSys.addWidget(self.rbtDec)
        self.lytNumSys.addWidget(self.rbtHex)
        self.lytNumSys.addWidget(self.rbtOct)
        self.lytNumSys.addWidget(self.rbtBin)

        self.rbtDec.toggled.connect(self.evt_rbt_clicked)  
        self.rbtHex.toggled.connect(self.evt_rbt_clicked)  
        self.rbtOct.toggled.connect(self.evt_rbt_clicked)  
        self.rbtBin.toggled.connect(self.evt_rbt_clicked)        

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.spbInt)
        self.lytMain.addWidget(self.lcd)
        self.lytMain.addLayout(self.lytNumSys)

        self.setLayout(self.lytMain)

    def evt_rbt_clicked(self):
        sender = self.sender()
        if sender.text() == "Dec":
            self.lcd.setDecMode()
        elif sender.text() == "Hex":
            self.lcd.setHexMode()
        elif sender.text() == "Oct":
            self.lcd.setOctMode()
        elif sender.text() == "Bin":
            self.lcd.setBinMode()
    
    def evt_spbInt_valueChnaged(self, val):
        self.lcd.display(val)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
