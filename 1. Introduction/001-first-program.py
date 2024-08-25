import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDialog,QMainWindow

app = QApplication(sys.argv)

dlgMain = QWidget()
# dlgMain = QDialog()
# dlgMain = QMainWindow()
dlgMain.setWindowTitle("My Gui")
dlgMain.show()

sys.exit(app.exec_())