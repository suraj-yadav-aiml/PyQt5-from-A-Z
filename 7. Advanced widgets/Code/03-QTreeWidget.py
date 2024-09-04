import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(1500, 900)

        ##### Create Widget
        self.trwQt = QTreeWidget()
        self.trwQt.setColumnCount(3)
        self.trwQt.setHeaderLabels(["Qt Class","Methods","Signals"])
        self.trwQt.itemDoubleClicked.connect(self.evt_trwQt_dblClicked)

        self.populate_tree()
        
        self.trwQt.sortItems(0, Qt.AscendingOrder) # 0 -> Sort using 1 column
        self.trwQt.setColumnWidth(0, 200)
        self.trwQt.expandItem(self.twiQWidget)

        self.cmbParents = QComboBox()
        lstClasses = get_all_items(self.trwQt)
        lstClasses.sort()
        for cls in lstClasses:
            self.cmbParents.addItem(cls.text(0))
        
        self.ledClassName = QLineEdit("Q")

        self.btnAddClass = QPushButton("Add Class")
        self.btnAddClass.clicked.connect(self.evt_btnAddClass_clicked)

        ##### Setup Input
        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.trwQt)
        self.lytMain.addWidget(self.cmbParents)
        self.lytMain.addWidget(self.ledClassName)
        self.lytMain.addWidget(self.btnAddClass)

        self.setLayout(self.lytMain)
    
    def populate_tree(self):

        ##### Create Top level items
        self.twiQWidget = QTreeWidgetItem(self.trwQt, ['QWidget Module'])
        self.twiQGui = QTreeWidgetItem(self.trwQt, ['QGui Module'])
        self.twiQCore = QTreeWidgetItem(self.trwQt, ['QCore Module'])

        ##### Add sub-items to QWidget Module
        lstQtWidget = ["QDialog", "QLabel", "QLineEdit", "QTextEdit", "QGroupBox", "QFrame"]
        for cls in lstQtWidget:
            self.twiQWidget.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(25))]))
        
        ##### Add Subitems to QGui
        lstQtGui = ["QBitmap", "QColor", "QFont", "QIcon", "QImage"]
        for cls in lstQtGui:
            self.twiQGui.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(25))]))
        

        ##### Add subitems to QtCore Module
        lstQtCore = ["QThread", "QDateTime", "QPixmap", "QUrl", "QFile"]
        for cls in lstQtCore:
            self.twiQCore.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(25))]))
        

        ##### Add subitems to Qdialog
        twi = self.trwQt.findItems("QDialog", Qt.MatchRecursive)[0]
        lstQDialog = ["QFileDialog", "QColorDialog", "QFontDialog", "QMessageBox"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls,str(random.randrange(25)), str(random.randrange(25))]))
        
        ###### add subitems to QFrame
        twi = self.trwQt.findItems("QFrame", Qt.MatchRecursive)[0]
        lstQFrame = ["QLabel", "QLCDNumber", "QStackedWidget", "QToolBox"]
        for cls in lstQFrame:
            twi.addChild(QTreeWidgetItem([cls,str(random.randrange(25)), str(random.randrange(25))]))
    
    def evt_trwQt_dblClicked(self, twi, col):
        QMessageBox.information(self,"Qt Class",f"You choose the {twi.text(0)} class")
    
    def evt_btnAddClass_clicked(self):
        ans = QMessageBox.question(self, "Add Class", "Are you sure that you want to add {} to {}".format(self.ledClassName.text(), self.cmbParents.currentText()))
        if ans == QMessageBox.Yes:
            twi = self.trwQt.findItems(self.cmbParents.currentText(), Qt.MatchRecursive)[0]
            twi.addChild(QTreeWidgetItem([self.ledClassName.text(), str(random.randrange(25)), str(random.randrange(25))]))

            self.cmbParents.addItem(self.ledClassName.text())

            
    
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
