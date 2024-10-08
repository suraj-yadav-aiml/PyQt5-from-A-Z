import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        ####  Create Widgets
        self.cmbSelector = QComboBox()
        self.cmbSelector.addItems(["General", "Species", "Location", "Surveys"])
        self.cmbSelector.currentIndexChanged.connect(self.evt_cmbSelector_changed)

        self.wdgGeneral = QWidget()
        self.wdgSpecies = QWidget()
        self.wdgLocation = QWidget()
        self.wdgSurveys = QWidget()

        ######  General Widgets
        self.lblNestID = QLabel("34")
        self.dteFound = QDateTimeEdit(QDate(2016, 5, 13))
        self.dteLast = QDateTimeEdit(QDate(2020, 4, 14))
        self.chkActive = QCheckBox()

        ########  Species widgets
        self.cmbSpecies = QComboBox()
        self.cmbSpecies.addItem("Red-tailed Hawk", 800)
        self.cmbSpecies.addItem("Swainsons Hawk", 400)
        self.cmbSpecies.addItem("Other", 1600)

        self.ledSpecies = QLineEdit()
        self.spbBuffer = QSpinBox()
        self.spbBuffer.setValue(800)

        ###########  Location Widget
        self.spbLatitude = QDoubleSpinBox()
        self.spbLongitude = QDoubleSpinBox()

        ###########   Survey Widget
        self.lstSurveys = QListWidget()
        self.lstSurveys.addItem("03/24/2020 - MSM - INACTIVE")
        self.lstSurveys.addItem("03/30/2020 - MSM - INACTIVE")
        self.lstSurveys.addItem("04/07/2020 - MSM - INACTIVE")
        self.lstSurveys.addItem("04/14/2020 - MSM - ACTIVE!!")
        self.btnAddSurvey = QPushButton("Add Survey")

        self.setupLayout()

    def setupLayout(self):
        self.lytMain = QHBoxLayout()
        self.lytLeft = QVBoxLayout()
        self.lytRight = QStackedLayout()

        self.lytMain.addLayout(self.lytLeft)
        self.lytMain.addLayout(self.lytRight)

        ######  Add Widgets to leftLayout
        self.lytLeft.addWidget(self.cmbSelector)
        self.lytLeft.addStretch()

        #####   Add Stacked Widgets to rightLayout
        self.lytRight.addWidget(self.wdgGeneral)
        self.lytRight.addWidget(self.wdgSpecies)
        self.lytRight.addWidget(self.wdgLocation)
        self.lytRight.addWidget(self.wdgSurveys)

        ##### Setup General Widget
        self.lytGeneral = QFormLayout()
        self.lytGeneral.addRow("Nest ID:", self.lblNestID)
        self.lytGeneral.addRow("Date Found:", self.dteFound)
        self.lytGeneral.addRow("Date Last Surveyed:", self.dteLast)
        self.lytGeneral.addRow("Currently Active", self.chkActive)
        self.wdgGeneral.setLayout(self.lytGeneral)

        ##### Setup Species Widget
        self.lytSpecies = QFormLayout()
        self.lytSpecies.addRow("Species:", self.cmbSpecies)
        self.lytSpecies.addRow("Species:", self.ledSpecies)
        self.lytSpecies.addRow("Buffer:", self.spbBuffer)
        self.spbBuffer.setSuffix(" m")
        self.wdgSpecies.setLayout(self.lytSpecies)

        ##### Setup Location Widget
        self.lytLocation = QFormLayout()
        self.lytLocation.addRow("Latitude:", self.spbLatitude)
        self.lytLocation.addRow("Longitude:", self.spbLongitude)
        self.wdgLocation.setLayout(self.lytLocation)

        ##### Setup Surveys Widget
        self.lytSurveys = QVBoxLayout()
        self.lytSurveys.addWidget(self.lstSurveys)
        self.lytSurveys.addWidget(self.btnAddSurvey)
        self.wdgSurveys.setLayout(self.lytSurveys)

        self.setLayout(self.lytMain)

    def evt_cmbSelector_changed(self, idx):
        self.lytRight.setCurrentIndex(idx)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
