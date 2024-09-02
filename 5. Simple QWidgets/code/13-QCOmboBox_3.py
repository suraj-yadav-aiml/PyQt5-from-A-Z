import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500,500)

        self.cmbStates = QComboBox(self)
        self.cmbStates.move(50,50)
        
        self.cmbStates.addItem("Alabama", {"ab":"AL", "pop":4000000})
        self.cmbStates.addItem("Alaska", {"ab":"AK", "pop":500000})
        self.cmbStates.addItem("Arizona", {"ab":"AZ", "pop":7000000})
        self.cmbStates.addItem("Arkansas", {"ab":"AR", "pop":3000000})
        self.cmbStates.addItem("Mississippi", {"ab":"MS", "pop":5000000})
        self.cmbStates.addItem("Missouri", {"ab":"MO", "pop":5000000})
        self.cmbStates.addItem("Minnesota", {"ab":"MN", "pop":6000000})
        self.cmbStates.addItem("Michigan", {"ab":"MI", "pop":10000000})

        self.lblPop = QLabel("Population: 4000000", self)
        self.lblPop.move(180, 55)

        self.cmbStates.currentIndexChanged.connect(self.evt_cmbStates_changed)
        self.cmbStates.highlighted.connect(self.evt_cmbStates_highlighted)

    def evt_cmbStates_changed(self, idx):
        data = self.cmbStates.itemData(idx) 
        QMessageBox.information(self, "Information", f"You selected : {data['ab']}\nWhich has a popluation of: {data['pop']}")
    
    def evt_cmbStates_highlighted(self,idx):
        self.lblPop.setText(f"Population: {self.cmbStates.itemData(idx)['pop']}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
