import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(1500, 900)

        ######  Create Widgets
        self.trwQt = QTreeWidget()
        self.trwQt.setColumnCount(1)
        self.trwQt.setHeaderLabels(["Qt Class"])
        self.trwQt.itemDoubleClicked.connect(self.evt_trwQt_dblClicked)

        self.populateTree()

        self.trwQt.sortItems(0, Qt.AscendingOrder)
        self.trwQt.setColumnWidth(0, 150)
        self.trwQt.expandItem(self.twiQWidget)

        self.cmbParents = QComboBox()
        lstClasses = get_all_items(self.trwQt)
        lstClasses.sort()
        for cls in lstClasses:
            self.cmbParents.addItem(cls.text(0))

        self.ledClassName = QLineEdit("Q")

        self.btnAddClass = QPushButton("Add Class")
        self.btnAddClass.clicked.connect(self.evt_btnAddClass_clicked)

        ######   lytWev Widgets

        self.wev = QWebEngineView()
        self.wev.setUrl(QUrl.fromUserInput("https://doc.qt.io/qt-5/qtmodules.html"))

        self.btnForward = QPushButton(">>")
        self.btnForward.clicked.connect(self.wev.forward)

        self.btnBack = QPushButton("<<")
        self.btnBack.clicked.connect(self.wev.back)

        self.btnHome = QPushButton("Home")
        self.btnHome.clicked.connect(self.evt_btnHome_clicked)

        ######  Setup layout
        self.lytMain = QHBoxLayout()

        self.lytTree = QVBoxLayout()
        self.lytTree.addWidget(self.trwQt)
        self.lytTree.addWidget(self.cmbParents)
        self.lytTree.addWidget(self.ledClassName)
        self.lytTree.addWidget(self.btnAddClass)

        self.lytButtons = QHBoxLayout()
        self.lytButtons.addWidget(self.btnBack)
        self.lytButtons.addWidget(self.btnForward)
        self.lytButtons.addWidget(self.btnHome)

        self.lytWev = QVBoxLayout()
        self.lytWev.addWidget(self.wev)
        self.lytWev.addLayout(self.lytButtons)

        self.lytMain.addLayout(self.lytTree, 20)
        self.lytMain.addLayout(self.lytWev, 80)

        self.setLayout(self.lytMain)

    def populateTree(self):
        ##### Create top level items

        self.twiQWidget = QTreeWidgetItem(self.trwQt, ["QWidget Module"])
        self.twiQGui = QTreeWidgetItem(self.trwQt, ["QGui Module"])
        self.twiQCore = QTreeWidgetItem(self.trwQt, ["QCore Module"])

        ##### Add subItems to QWidget Module
        lstQtWidget = ["QDialog", "QLabel", "QLineEdit", "QTextEdit", "QGroupBox", "QFrame"]
        for cls in lstQtWidget:
            self.twiQWidget.addChild(QTreeWidgetItem([cls]))

        ##### Add Subitems to QGui
        lstQtGui = ["QBitmap", "QColor", "QFont", "QIcon", "QImage"]
        for cls in lstQtGui:
            self.twiQGui.addChild(QTreeWidgetItem([cls]))

        #### Add subitems to QtCore Module
        lstQtCore = ["QThread", "QDateTime", "QPixmap", "QUrl", "QFile"]
        for cls in lstQtCore:
            self.twiQCore.addChild(QTreeWidgetItem([cls]))

        ##### Add subitems to Qdialog
        twi = self.trwQt.findItems("QDialog", Qt.MatchRecursive)[0]
        lstQDialog = ["QFileDialog", "QColorDialog", "QFontDialog", "QMessageBox"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls]))

        ###### add subitems to QFrame
        twi = self.trwQt.findItems("QFrame", Qt.MatchRecursive)[0]
        lstQFrame = ["QLabel", "QLCDNumber", "QStackedWidget", "QToolBox"]
        for cls in lstQFrame:
            twi.addChild(QTreeWidgetItem([cls]))

    #####  Event handlers
    def evt_trwQt_dblClicked(self, twi, col):
        url = f"https://doc.qt.io/qt-5/{twi.text(0).lower()}.html"
        self.wev.setUrl(QUrl.fromUserInput(url))

    def evt_btnAddClass_clicked(self):
        ans = QMessageBox.question(self, "Add Class", "Are you sure that you want to add {} to {}".format(self.ledClassName.text(), self.cmbParents.currentText()))
        if ans == QMessageBox.Yes:
            twi = self.trwQt.findItems(self.cmbParents.currentText(), Qt.MatchRecursive)[0]
            twi.addChild(QTreeWidgetItem([self.ledClassName.text()]))

            self.cmbParents.addItem(self.ledClassName.text())
            self.cmbParents.model().sort(0)


            

    def evt_btnHome_clicked(self):
        self.wev.setUrl(QUrl.fromUserInput("https://doc.qt.io/qt-5/qtmodules.html"))

#######  TWO FUNCTIONS REQUIRED TO RECURSIVELY RETURN ALL ITEMS

def get_subtree_nodes(tree_widget_item):
    """Returns all QTreeWidgetItems in the subtree rooted at the given node."""
    nodes = []
    nodes.append(tree_widget_item)
    for i in range(tree_widget_item.childCount()):
        nodes.extend(get_subtree_nodes(tree_widget_item.child(i)))
    return nodes

def get_all_items(tree_widget):
    """Returns all QTreeWidgetItems in the given QTreeWidget."""
    all_items = []
    for i in range(tree_widget.topLevelItemCount()):
        top_item = tree_widget.topLevelItem(i)
        all_items.extend(get_subtree_nodes(top_item))
    return all_items


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
