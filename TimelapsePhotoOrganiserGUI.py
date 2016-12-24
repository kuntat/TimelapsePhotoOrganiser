#!/usr/bin/env python
##
## TimelapsePhotoOrganiser.py
## TimelapsePhotoOrganiser
##
## Created by Kun Tat on 26/8/16.
##


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from TimelapsePhotoOrganiserModel import *

class timelapsePhotoOrganiserGUI(QMainWindow):
    directory = "directory:                 "
    
    def __init__(self, parent = None):
        super(timelapsePhotoOrganiserGUI, self).__init__(parent)

        # browse button
        self.browseBtn = QPushButton("Browse")
        self.browseBtn.clicked.connect(self.getfilesDialog)

        # result label
        self.labelFolder = QLabel()
        self.labelFolder.setText(self.directory)

        # checkbox for checking dimensions
        self.checkboxDimensions = QCheckBox("Check Dimensions?")
        self.checkboxDimensions.toggled
        
        # ok and clear buttons
        self.okBtn = QPushButton("Ok")
        self.okBtn.clicked.connect(self.runProgram)
        self.clearBtn = QPushButton("Clear")
        self.clearBtn.clicked.connect(self.clearDirectory)

        # status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        # adding widget
        layoutTop = QHBoxLayout()
        layoutTop.addWidget(self.labelFolder)        
        layoutTop.addWidget(self.browseBtn)

        layoutBottom = QHBoxLayout()
        layoutBottom.addWidget(self.okBtn)
        layoutBottom.addWidget(self.clearBtn)

        layout = QVBoxLayout()
        layout.addLayout(layoutTop)
        layout.addWidget(self.checkboxDimensions)
        layout.addLayout(layoutBottom)

        window = QWidget()
        window.setLayout(layout)
        self.setWindowTitle("Timelapse Photo Organiser")
        self.setCentralWidget(window)

    def getfilesDialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)

        if dialog.exec_():
            filenames = dialog.selectedFiles()
            self.directory = filenames[0]
            self.labelFolder.setText("directory: " + self.directory)
            self.labelFolder.repaint()

    def runProgram(self):
        self.statusBar.showMessage("Wait for it...")
        if organise(self.directory, self.checkboxDimensions.isChecked()):
            self.okDialog(True)
            self.statusBar.showMessage("Done!", 5000)
        else:
            self.okDialog(False)
            self.statusBar.clearMessage()


    def okDialog(self, booleanValue):
        runDialog = QDialog()
        runDialogLabel = QLabel(runDialog)
        if booleanValue:
            runDialogLabel.setText("Done!")
        else:
            runDialogLabel.setText("There is something wrong with the folder you selected.\nPlease check and try again.")
        runDialogBtn = QPushButton("Ok", runDialog)
        runDialogBtn.clicked.connect(runDialog.close)
        runDialogLayout = QVBoxLayout()
        runDialogLayout.addWidget(runDialogLabel)
        runDialogLayout.addWidget(runDialogBtn)
        runDialog.setLayout(runDialogLayout)
        runDialog.exec_()

    def clearDirectory(self):
        self.directory = "directory:                 "
        self.labelFolder.setText(self.directory)
        self.labelFolder.repaint()
            

def main():
    app = QApplication(sys.argv)
    ex = timelapsePhotoOrganiserGUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
