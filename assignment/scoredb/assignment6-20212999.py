# 박재우 - 20212999

import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(str(self.KeyCb.currentText()))

    def setUI(self):
        layout1 = QHBoxLayout()
        nameL = QLabel('Name:')
        ageL = QLabel('Age:')
        scoreL = QLabel('Score:')
        self.nameE = QLineEdit()
        self.ageE = QLineEdit()
        self.scoreE = QLineEdit()

        list1 = [nameL, self.nameE, ageL, self.ageE, scoreL, self.scoreE]
        for l in list1:
            layout1.addWidget(l)

        layout2 = QHBoxLayout()
        AmountL = QLabel('Amount:')
        KeyL = QLabel('Key:')
        self.AmountE = QLineEdit()
        self.KeyCb = QComboBox()
        self.KeyCb.addItem('Name')
        self.KeyCb.addItem('Age')
        self.KeyCb.addItem('Score')
        layout2.addStretch(1)
        list2 = [AmountL, self.AmountE, KeyL, self.KeyCb]
        for l in list2:
            layout2.addWidget(l)

        layout3 = QHBoxLayout()
        self.AddB = QPushButton('Add')
        self.DelB = QPushButton('Del')
        self.FindB = QPushButton('Find')
        self.IncB = QPushButton('Inc')
        self.ShowB = QPushButton('Show')

        list3 = [self.AddB, self.DelB, self.FindB, self.IncB, self.ShowB]
        layout3.addStretch(1)
        for l in list3:
            layout3.addWidget(l)

        layout4 = QHBoxLayout()
        ResultL = QLabel('Result :')
        layout4.addWidget(ResultL)

        layout5 = QVBoxLayout()
        self.ResultE = QTextEdit()
        layout5.addWidget(self.ResultE)

        EntryLayout = QVBoxLayout()
        EntryList = [layout1, layout2, layout3, layout4, layout5]
        for l in EntryList:
            EntryLayout.addLayout(l)

        self.setLayout(EntryLayout)

        self.AddB.clicked.connect(self.buttonClicked)
        self.DelB.clicked.connect(self.buttonClicked)
        self.FindB.clicked.connect(self.buttonClicked)
        self.IncB.clicked.connect(self.buttonClicked)
        self.ShowB.clicked.connect(self.buttonClicked)

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.setUI()
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == 'Add':
            self.ResultE.append(self.addScoreDB())
        elif sender.text() == 'Del':
            self.ResultE.append(self.delScoreDB())
        elif sender.text() == 'Find':
            self.ResultE.append(self.FindScoreDB())
        elif sender.text() == 'Inc':
            self.ResultE.append(self.IncScoreDB())
        else:
            self.ResultE.append(self.showScoreDB(str(self.KeyCb.currentText())))


    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def addScoreDB(self):
        record = {'Name': self.nameE.text(), 'Age': int(self.ageE.text()), 'Score': int(self.scoreE.text())}
        self.scoredb += [record]

        self.showScoreDB(str(self.KeyCb.currentText()))

    def delScoreDB(self):
        list = []
        for p in self.scoredb:
            if p['Name'] != str(self.nameE.text()):
                list.append(p)
            self.scoredb = list
        self.showScoreDB(str(self.KeyCb.currentText()))

    def FindScoreDB(self):
        list = []
        for p in self.scoredb:
            if p['Name'] == str(self.nameE.text()):
                list.append(p)

        key = str(self.KeyCb.currentText())
        self.ResultE.clear()
        for p in sorted(list, key=lambda person: person[key]):
            s = ""
            for attr in sorted(p):
                s += (attr + ": " + str(p[attr]) + "          ")
            self.ResultE.append(str(s))

    def IncScoreDB(self):
        for p in self.scoredb:
            if p['Name'] == str(self.nameE.text()):
                p['Score'] = str(int(p['Score']) + int(self.AmountE.text()))
        self.showScoreDB(str(self.KeyCb.currentText()))

    def showScoreDB(self, key):
        self.ResultE.clear()

        for p in sorted(self.scoredb, key=lambda person: person[key]):
            s = ""
            strFormat = '%-15s%-20s%-15s'
            strOut = ""

            for attr in sorted(p):
                s += (attr + ": " + str(p[attr]) + "   ")
            s_sp = s.split("   ")
            strOut += strFormat % (s_sp[0], s_sp[1], s_sp[2])
            ##print(strOut)
            self.ResultE.append(str(strOut))
        pass

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

