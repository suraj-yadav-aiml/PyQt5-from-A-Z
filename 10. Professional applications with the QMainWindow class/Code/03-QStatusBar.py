import sys
from PyQt5.QtWidgets import *
from ui.QStatusBar_ui import *

class MenuMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)

        self.prg = QProgressBar()
        self.prg.setValue(50)
        self.prg.setStyle(QStyleFactory.create("Windows"))
        # self.statusbar.addWidget(self.prg)
        self.statusbar.addPermanentWidget(self.prg)

        self.actionOpen.triggered.connect(self.evt_open_triggered)
        self.actionQuit.triggered.connect(self.evt_quit_triggered)
        self.btnDisplay.clicked.connect(self.evt_btnDisplay_clicked)
    
    def evt_open_triggered(self):
        sFile, sFilter = QFileDialog.getOpenFileName(self, "Open", "ui", "User Interface Files(*.ui)")
        if sFile:
            print(sFile)
        else:
            print("CANCELED BY USER !!!")
    
    def evt_quit_triggered(self):
        sys.exit(0)
    
    def evt_btnDisplay_clicked(self):
        self.statusbar.showMessage(self.ledMessage.text(),self.sbxMsec.value())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mnuMain = MenuMain()
    mnuMain.show()
    sys.exit(app.exec_())
