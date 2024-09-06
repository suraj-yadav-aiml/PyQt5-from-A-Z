import sys
from PyQt5.QtWidgets import *
from ui.menu_demo_ui import *

class MenuMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mnuMain = MenuMain()
    mnuMain.show()
    sys.exit(app.exec_())
