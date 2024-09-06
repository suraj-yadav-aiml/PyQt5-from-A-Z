import sys
from PyQt5.QtWidgets import *
from ui.menu_demo_ui import *

class MenuMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)

        self.actionOpen.triggered.connect(self.evt_open_triggered)
        self.actionQuit.triggered.connect(self.evt_quit_triggered)
    
    def evt_open_triggered(self):
        sFile, sFilter = QFileDialog.getOpenFileName(self, "Open", "ui", "User Interface Files(*.ui)")
        if sFile:
            print(sFile)
        else:
            print("CANCELED BY USER !!!")
    
    def evt_quit_triggered(self):
        sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mnuMain = MenuMain()
    mnuMain.show()
    sys.exit(app.exec_())
