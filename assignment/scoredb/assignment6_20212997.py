import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        self.nameLabel = QLabel("Name: ")
        self.ageLabel = QLabel("Age: ")
        self.scoreLabel = QLabel("Score: ")
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()


        self.h1=QHBoxLayout()
        self.h1.addWidget(self.nameLabel)
        self.h1.addWidget(self.nameEdit)
        self.h1.addWidget(self.ageLabel)
        self.h1.addWidget(self.ageEdit)
        self.h1.addWidget(self.scoreLabel)
        self.h1.addWidget(self.scoreEdit)


        self.amountLabel = QLabel("Amount: ")
        self.amountEdit = QLineEdit()
        self.keyLabel=QLabel("Key: ")
        self.keyCombobox=QComboBox()
        self.keyCombobox.addItems(["Name", "Age", "Score"])

        self.h2=QHBoxLayout()
        self.h2.addStretch(1)
        self.h2.addWidget(self.amountLabel)
        self.h2.addWidget(self.amountEdit)
        self.h2.addWidget(self.keyLabel)
        self.h2.addWidget(self.keyCombobox)

        self.addButton = QPushButton("Add", self)
        self.addButton.clicked.connect(self.doAdd)
        self.delButton = QPushButton("Del", self)
        self.delButton.clicked.connect(self.doDel)
        self.findButton = QPushButton("Find", self)
        self.findButton.clicked.connect(self.doFind)
        self.incButton = QPushButton("Inc", self)
        self.incButton.clicked.connect(self.doInc)
        self.showButton = QPushButton("Show", self)
        self.showButton.clicked.connect(self.doShow)

        self.h3=QHBoxLayout()
        self.h3.addStretch(1)
        self.h3.addWidget(self.addButton)
        self.h3.addWidget(self.delButton)
        self.h3.addWidget(self.findButton)
        self.h3.addWidget(self.incButton)
        self.h3.addWidget(self.showButton)

        self.v1=QVBoxLayout()
        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)

        self.resultLabel=QLabel("Result: ")
        self.resultOutput = QTextEdit()
        self.resultOutput.setReadOnly(True)

        self.v1.addWidget(self.resultLabel)
        self.v1.addWidget(self.resultOutput)

        self.setLayout(self.v1)
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
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

    def showScoreDB(self):
        outstr=''

        for i in self.scoredb:
            #outstr+='Age : ' + str(i['Age']) + '\tName : ' + i['Name'] + '\t\tScore : ' + str(i['Score'])
            #outstr += '\n'
            for j in i:
                outstr += str(j) + ' : ' + str(i[j]) + '   '
            outstr += '\n'
        self.resultOutput.setText(outstr)

    def doAdd(self):
        if self.nameEdit.text() != '' and self.ageEdit.text() != '' and self.scoreEdit.text() != '':
            self.scoredb.append({'Name':self.nameEdit.text(),'Age':int(self.ageEdit.text()),'Score':int(self.scoreEdit.text())})
            self.showScoreDB()

    def doDel(self):
        list = []
        for p in self.scoredb:
            if p['Name'] != self.nameEdit.text():
                list.append(p)
        self.scoredb = list
        self.showScoreDB()

    def doFind(self):
        print(self.nameLabel.text())
        showstr=''
        for i in self.scoredb:
            if i['Name'] == self.nameEdit.text():
                for j in i:
                    showstr+=str(j)+' : '+str(i[j])+'\t'
                showstr+='\n'

        self.resultOutput.setText(showstr)

    def doInc(self):
        if self.amountEdit != '':
            for i in self.scoredb:
                if i['Name'] == self.nameEdit.text():
                    i['Score']+=int(self.amountEdit.text())
            self.showScoreDB()

    def doShow(self):
        showstr=''
        for p in sorted(self.scoredb, key=lambda person: person[self.keyCombobox.currentText()]):
            for j in p:
                showstr += str(j) + ' : ' + str(p[j]) + '\t'
            showstr += '\n'
        self.resultOutput.setText(showstr)

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

