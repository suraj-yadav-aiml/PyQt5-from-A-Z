import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500,500)

        self.cmbStates = QComboBox(self)
        self.cmbStates.move(50,50)
        
        self.cmbStates.addItem("Alabama", "AL")
        self.cmbStates.addItem("Alaska", "AK")
        self.cmbStates.addItem("Michigan", "MI")
        self.cmbStates.addItem("Minnesota", "MN")
        self.cmbStates.addItem("Missouri", "MO")
        self.cmbStates.addItem("Mississippi", "MS")

        self.cmbStates.currentIndexChanged.connect(self.evt_cmbStates_changed)

    def evt_cmbStates_changed(self, idx):
        QMessageBox.information(self, "Information", f"You selected : {self.cmbStates.itemData(idx)}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
