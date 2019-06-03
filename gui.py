from PyQt5 import QtCore, QtGui, QtWidgets
from cortexmulator.cortexm0lator import CortexM0lator

class Ui_CortexM0UI(object):
    def setupUi(self, CortexM0UI):
        CortexM0UI.setObjectName("CortexM0UI")
        CortexM0UI.setEnabled(True)
        CortexM0UI.setFixedSize(380, 518)
        self.filename = None
        self.m = CortexM0lator()
        self.centralwidget = QtWidgets.QWidget(CortexM0UI)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 30, 241, 431))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 30, 111, 32))
        self.pushButton.setObjectName("pushButton")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(260, 60, 111, 32))
        self.button2.setObjectName("button2")
        CortexM0UI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CortexM0UI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        CortexM0UI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CortexM0UI)
        self.statusbar.setObjectName("statusbar")
        CortexM0UI.setStatusBar(self.statusbar)
        self.actionLoad_hex_file = QtWidgets.QAction(CortexM0UI)
        self.actionLoad_hex_file.setObjectName("actionLoad_hex_file")
        self.menuFile.addAction(self.actionLoad_hex_file)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.setNativeMenuBar(False)
        self.error_dialog = QtWidgets.QErrorMessage()

        self.retranslateUi(CortexM0UI)
        QtCore.QMetaObject.connectSlotsByName(CortexM0UI)

        self.pushButton.clicked.connect(self.run)
        self.button2.clicked.connect(self.getRegisters)
        self.actionLoad_hex_file.triggered.connect(self.setFilePath)

    def retranslateUi(self, CortexM0UI):
        _translate = QtCore.QCoreApplication.translate
        CortexM0UI.setWindowTitle(_translate("CortexM0UI", "CortexM0lator"))
        self.label.setText(_translate("CortexM0UI", "Registers"))
        self.pushButton.setText(_translate("CortexM0UI", "Run emulation"))
        self.button2.setText(_translate("CortexM0UI", "Get registers"))
        self.menuFile.setTitle(_translate("CortexM0UI", "File"))
        self.actionLoad_hex_file.setText(_translate("CortexM0UI", "Load hex file"))
    
    def  run(self):
        if self.filename is not None:
            self.m.read_hex_data(self.filename)
            self.listView.clear()
            for key in self.m.memory._registers:
                value = key + ': ' + '0x' + str(hex(self.m.memory._registers[key])[2:].zfill(4))
                self.listView.addItem(value)
            self.m.run()
        else: 
            self.error_dialog.showMessage('File not loaded!')
    
    def setFilePath(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select hex file", "", "Intel HEX Files (*.hex)")

    def getRegisters(self):
        self.listView.clear()
        for key in self.m.memory._registers:
            value = key + ': ' + '0x' + str(hex(self.m.memory._registers[key])[2:].zfill(4))
            self.listView.addItem(value)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CortexM0UI = QtWidgets.QMainWindow()
    ui = Ui_CortexM0UI()
    ui.setupUi(CortexM0UI)
    CortexM0UI.show()
    sys.exit(app.exec_())
