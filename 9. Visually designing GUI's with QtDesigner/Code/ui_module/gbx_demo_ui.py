# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Suraj\LearningPath\Python GUI Projects\PyQt5 From A-Z 2020-9\9. Visually designing GUI's with QtDesigner\Code\ui\gbx_demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(853, 240)
        Dialog.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(255, 165, 254)\n"
"}")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 851, 241))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.lytMain = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.lytMain.setContentsMargins(0, 0, 0, 0)
        self.lytMain.setSpacing(7)
        self.lytMain.setObjectName("lytMain")
        self.gbxCheckable = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.gbxCheckable.setCheckable(True)
        self.gbxCheckable.setObjectName("gbxCheckable")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.gbxCheckable)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 251, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.rbtCheckTrue = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtCheckTrue.setChecked(True)
        self.rbtCheckTrue.setObjectName("rbtCheckTrue")
        self.verticalLayout.addWidget(self.rbtCheckTrue, 0, QtCore.Qt.AlignHCenter)
        self.rbtCheckFalse = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtCheckFalse.setObjectName("rbtCheckFalse")
        self.verticalLayout.addWidget(self.rbtCheckFalse, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.lytMain.addWidget(self.gbxCheckable)
        self.gbxFlat = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.gbxFlat.setFlat(True)
        self.gbxFlat.setObjectName("gbxFlat")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.gbxFlat)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 271, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.rbtFlatTrue = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbtFlatTrue.setChecked(True)
        self.rbtFlatTrue.setObjectName("rbtFlatTrue")
        self.verticalLayout_2.addWidget(self.rbtFlatTrue, 0, QtCore.Qt.AlignHCenter)
        self.rbtFlatFalse = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbtFlatFalse.setObjectName("rbtFlatFalse")
        self.verticalLayout_2.addWidget(self.rbtFlatFalse, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.lytMain.addWidget(self.gbxFlat)
        self.gbxAlignment = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.gbxAlignment.setObjectName("gbxAlignment")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.gbxAlignment)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 261, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.rbtLeft = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.rbtLeft.setChecked(True)
        self.rbtLeft.setObjectName("rbtLeft")
        self.verticalLayout_3.addWidget(self.rbtLeft, 0, QtCore.Qt.AlignHCenter)
        self.rbtCenter = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.rbtCenter.setObjectName("rbtCenter")
        self.verticalLayout_3.addWidget(self.rbtCenter, 0, QtCore.Qt.AlignHCenter)
        self.rbtRght = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.rbtRght.setObjectName("rbtRght")
        self.verticalLayout_3.addWidget(self.rbtRght, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.lytMain.addWidget(self.gbxAlignment)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.gbxCheckable.setTitle(_translate("Dialog", "Checkable"))
        self.rbtCheckTrue.setText(_translate("Dialog", "True"))
        self.rbtCheckFalse.setText(_translate("Dialog", "False"))
        self.gbxFlat.setTitle(_translate("Dialog", "Flat"))
        self.rbtFlatTrue.setText(_translate("Dialog", "True"))
        self.rbtFlatFalse.setText(_translate("Dialog", "False"))
        self.gbxAlignment.setTitle(_translate("Dialog", "Alignment"))
        self.rbtLeft.setText(_translate("Dialog", "Align Left"))
        self.rbtCenter.setText(_translate("Dialog", "Align Center"))
        self.rbtRght.setText(_translate("Dialog", "Align Right"))
