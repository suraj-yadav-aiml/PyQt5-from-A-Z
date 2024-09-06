import sys, os
from PyQt5.QtWidgets import *
from ui.QSplitter_ui import *
import treewidget 

class MenuMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)

        self.lytMain = QHBoxLayout()
        self.centralwidget.setLayout(self.lytMain)
        self.lytMain.addWidget(self.splitter)

        self.prg = QProgressBar()
        self.prg.setValue(50)
        self.prg.setStyle(QStyleFactory.create("Windows"))
        # self.statusbar.addWidget(self.prg)
        self.statusbar.addPermanentWidget(self.prg)

        self.listWidget.addItems(os.listdir("./ui"))

        self.actionOpen.triggered.connect(self.evt_open_triggered)
        self.actionQuit.triggered.connect(self.evt_quit_triggered)
        self.listWidget.itemDoubleClicked.connect(self.evt_lst_dbl)

        #### Mulit Dialog Window Signal
        self.actionHelp.triggered.connect(self.evt_help_triggered)
        
    
    def evt_open_triggered(self):
        sFile, sFilter = QFileDialog.getOpenFileName(self, "Open", "ui", "Any files Files(*.*)")
        if sFile:
            with open(sFile) as f:
                self.plainTextEdit.setPlainText(f.read())
        else:
            print("CANCELED BY USER !!!")
    
    def evt_quit_triggered(self):
        sys.exit(0)
    
    def evt_lst_dbl(self, lwi):
        # QMessageBox.information(self,"File", f"You selected '{lwi.text()}'")
        with open(f"./ui/{lwi.text()}") as f:
            file_content = f.read()
        
        self.plainTextEdit.setPlainText(file_content)
    
    def evt_help_triggered(self):
        dlgTre = treewidget.DlgMain()
        dlgTre.show()
        dlgTre.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mnuMain = MenuMain()
    mnuMain.show()
    sys.exit(app.exec_())
