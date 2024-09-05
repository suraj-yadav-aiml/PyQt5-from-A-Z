import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import os

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/gbx_demo.ui", self) 
        # uic.loadUi(os.path.join(".","ui","gbx_demo.ui"),self)

        self.rbtCheckTrue.toggled.connect(self.evt_rbtCheckTrue_toggled)
        self.rbtFlatTrue.toggled.connect(self.evt_rbtFlatTrue_toggled)
        self.rbtLeft.toggled.connect(self.evt_rbtLeft_toggled)
        self.rbtRght.toggled.connect(self.evt_rbtRight_toggled)
        self.rbtCenter.toggled.connect(self.evt_rbtCenter_toggled)

    def evt_rbtCheckTrue_toggled(self, chk):
        self.gbxCheckable.setCheckable(chk)
    
    def evt_rbtFlatTrue_toggled(self, chk):
        self.gbxFlat.setFlat(chk)
    
    def evt_rbtLeft_toggled(self, chk):
        self.gbxAlignment.setAlignment(Qt.AlignLeft)
        self.gbxAlignment.setTitle("Left")
    
    def evt_rbtRight_toggled(self, chk):
        self.gbxAlignment.setAlignment(Qt.AlignRight)
        self.gbxAlignment.setTitle("Right")

    def evt_rbtCenter_toggled(self, chk):
        self.gbxAlignment.setAlignment(Qt.AlignCenter)
        self.gbxAlignment.setTitle("Center")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
