# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Suraj\LearningPath\Python GUI Projects\PyQt5 From A-Z 2020-9\10. Professional applications with the QMainWindow class\Code\ui\QSplitter.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(3, 8, 631, 381))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listWidget = QtWidgets.QListWidget(self.splitter)
        self.listWidget.setObjectName("listWidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.splitter)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExamples = QtWidgets.QMenu(self.menubar)
        self.menuExamples.setObjectName("menuExamples")
        self.menuDialog = QtWidgets.QMenu(self.menuExamples)
        self.menuDialog.setObjectName("menuDialog")
        self.menuQMessageBox = QtWidgets.QMenu(self.menuDialog)
        self.menuQMessageBox.setObjectName("menuQMessageBox")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Suraj\\LearningPath\\Python GUI Projects\\PyQt5 From A-Z 2020-9\\10. Professional applications with the QMainWindow class\\Code\\ui\\../../../2. Installing PyQt5/CODE/fotos/SidebarGenericFile.icns"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\Suraj\\LearningPath\\Python GUI Projects\\PyQt5 From A-Z 2020-9\\10. Professional applications with the QMainWindow class\\Code\\ui\\../../../2. Installing PyQt5/CODE/fotos/SidebarGenericFolder.icns"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\Suraj\\LearningPath\\Python GUI Projects\\PyQt5 From A-Z 2020-9\\10. Professional applications with the QMainWindow class\\Code\\ui\\../../../2. Installing PyQt5/CODE/fotos/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSimple_Widgets = QtWidgets.QAction(MainWindow)
        self.actionSimple_Widgets.setObjectName("actionSimple_Widgets")
        self.actionLayouts = QtWidgets.QAction(MainWindow)
        self.actionLayouts.setObjectName("actionLayouts")
        self.actionAdvanced_Widgets = QtWidgets.QAction(MainWindow)
        self.actionAdvanced_Widgets.setObjectName("actionAdvanced_Widgets")
        self.actionQDialogBox = QtWidgets.QAction(MainWindow)
        self.actionQDialogBox.setObjectName("actionQDialogBox")
        self.actionQFileDialog = QtWidgets.QAction(MainWindow)
        self.actionQFileDialog.setObjectName("actionQFileDialog")
        self.actionQColorDialog = QtWidgets.QAction(MainWindow)
        self.actionQColorDialog.setObjectName("actionQColorDialog")
        self.actioninformation = QtWidgets.QAction(MainWindow)
        self.actioninformation.setObjectName("actioninformation")
        self.actionquestion = QtWidgets.QAction(MainWindow)
        self.actionquestion.setObjectName("actionquestion")
        self.actioncritical = QtWidgets.QAction(MainWindow)
        self.actioncritical.setObjectName("actioncritical")
        self.actionwarning = QtWidgets.QAction(MainWindow)
        self.actionwarning.setObjectName("actionwarning")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("d:\\Suraj\\LearningPath\\Python GUI Projects\\PyQt5 From A-Z 2020-9\\10. Professional applications with the QMainWindow class\\Code\\ui\\../../../2. Installing PyQt5/CODE/fotos/HelpIcon.icns"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon3)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout_Menu = QtWidgets.QAction(MainWindow)
        self.actionAbout_Menu.setObjectName("actionAbout_Menu")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuQMessageBox.addAction(self.actioninformation)
        self.menuQMessageBox.addAction(self.actionquestion)
        self.menuQMessageBox.addAction(self.actioncritical)
        self.menuQMessageBox.addAction(self.actionwarning)
        self.menuDialog.addAction(self.menuQMessageBox.menuAction())
        self.menuDialog.addAction(self.actionQDialogBox)
        self.menuDialog.addAction(self.actionQFileDialog)
        self.menuDialog.addAction(self.actionQColorDialog)
        self.menuExamples.addAction(self.menuDialog.menuAction())
        self.menuExamples.addAction(self.actionSimple_Widgets)
        self.menuExamples.addAction(self.actionLayouts)
        self.menuExamples.addAction(self.actionAdvanced_Widgets)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout_Menu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExamples.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu Demo"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExamples.setTitle(_translate("MainWindow", "Examples"))
        self.menuDialog.setTitle(_translate("MainWindow", "Dialog"))
        self.menuQMessageBox.setTitle(_translate("MainWindow", "QMessageBox"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "Create New Project"))
        self.actionNew.setStatusTip(_translate("MainWindow", "New Project"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open File"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Click to exit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSimple_Widgets.setText(_translate("MainWindow", "Simple Widgets"))
        self.actionLayouts.setText(_translate("MainWindow", "Layouts"))
        self.actionAdvanced_Widgets.setText(_translate("MainWindow", "Advanced Widgets"))
        self.actionQDialogBox.setText(_translate("MainWindow", "QDialogBox"))
        self.actionQFileDialog.setText(_translate("MainWindow", "QFileDialog"))
        self.actionQColorDialog.setText(_translate("MainWindow", "QColorDialog"))
        self.actioninformation.setText(_translate("MainWindow", "information"))
        self.actionquestion.setText(_translate("MainWindow", "question"))
        self.actioncritical.setText(_translate("MainWindow", "critical"))
        self.actionwarning.setText(_translate("MainWindow", "warning"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout_Menu.setText(_translate("MainWindow", "About Menu"))
