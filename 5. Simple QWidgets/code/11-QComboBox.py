import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500,500)

        self.cmbStates = QComboBox(self)
        self.cmbStates.move(50,50)
        self.cmbStates.addItems(["AL", "AR", "MA", "MO", "MI"])

        self.cmbStates.currentTextChanged.connect(self.evt_cmbStates_changed)

    def evt_cmbStates_changed(self, text):
        QMessageBox.information(self, "Information", f"You selected : {text}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
