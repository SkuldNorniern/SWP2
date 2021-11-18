import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit,QErrorMessage)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(self.qlist.currentText())


    def initUI(self):
        self.setGeometry(300, 300, 500, 250)

        self.mainlayout=QVBoxLayout()
        self.nametbox=QLineEdit()
        self.agetbox=QLineEdit()
        self.scoretbox=QLineEdit()
        self.amounttbox=QLineEdit()
        self.resulttbox=QTextEdit()

        self.error_dialog = QErrorMessage()

        self.addbtn=QPushButton("Add")
        self.delbtn=QPushButton("Del")
        self.findbtn=QPushButton("Find")
        self.incbtn=QPushButton("Inc")
        self.showbtn=QPushButton("Show")

        self.addbtn.clicked.connect(self.btnclick)
        self.delbtn.clicked.connect(self.btnclick)
        self.findbtn.clicked.connect(self.btnclick)
        self.incbtn.clicked.connect(self.btnclick)
        self.showbtn.clicked.connect(self.btnclick)

        self.qlist=QComboBox()
        self.qlist.addItem("Name")
        self.qlist.addItem("Age")
        self.qlist.addItem("Score")

        ln1=QHBoxLayout()
        ln1.addWidget(QLabel("Name: "))
        ln1.addWidget(self.nametbox)
        ln1.addWidget(QLabel("Age: "))
        ln1.addWidget(self.agetbox)
        ln1.addWidget(QLabel("Score: "))
        ln1.addWidget(self.scoretbox)

        ln2=QHBoxLayout()
        ln2.addStretch(1)
        ln2.addWidget(QLabel("Amount: "))
        ln2.addWidget(self.amounttbox)
        ln2.addWidget(QLabel("Key: "))
        ln2.addWidget(self.qlist)

        ln3=QHBoxLayout()
        ln3.addStretch()
        ln3.addWidget(self.addbtn)
        ln3.addWidget(self.delbtn)
        ln3.addWidget(self.findbtn)
        ln3.addWidget(self.incbtn)
        ln3.addWidget(self.showbtn)

        ln4=QHBoxLayout()
        ln4.addWidget(QLabel("Result:"))

        ln5=QHBoxLayout()
        ln5.addWidget(self.resulttbox)

        self.mainlayout.addLayout(ln1)
        self.mainlayout.addLayout(ln2)
        self.mainlayout.addLayout(ln3)
        self.mainlayout.addLayout(ln4)
        self.mainlayout.addLayout(ln5)

        self.setLayout(self.mainlayout)
        self.setWindowTitle('Assignment6')
        self.show()

    def btnclick(self):
        sender = self.sender()
        try:
            if sender.text()=="Add":
                if len(self.nametbox.text()) ==0:
                    msg='Input name.'
                    self.error_dialog.showMessage(msg)
                    raise Exception(msg)
                if len(self.agetbox.text()) ==0:
                    msg='Input age.'
                    self.error_dialog.showMessage(msg)
                    raise Exception(msg)
                if len(self.scoretbox.text()) ==0:
                    msg='Input score.'
                    self.error_dialog.showMessage(msg)
                    raise Exception(msg)
                if not self.agetbox.text().isdigit():
                    msg='Imput the age in integer form.'
                    self.error_dialog.showMessage(msg)
                    raise Exception(msg)
                if not self.scoretbox.text().isdigit():
                    msg='Imput the score in integer form.'
                    self.error_dialog.showMessage(msg)
                    raise Exception(msg)
                record = {'Name': self.nametbox.text(), 'Age': int(self.agetbox.text()),'Score': int(self.scoretbox.text())}
                self.scoredb  += [record]
                self.writeScoreDB()
                self.showScoreDB(self.qlist.currentText())

            elif sender.text()=="Del":
                if len(self.nametbox.text()) ==0:
                    msg='Input name.'
                    self.error_dialog.showMessage(msg)
                    raise Exception(msg)
                for p in reversed(self.scoredb):
                        if p['Name'] == self.nametbox.text():
                            self.scoredb.remove(p)
                self.showScoreDB(self.qlist.currentText())

            elif sender.text()=="Find":
                if len(self.nametbox.text()) ==0:
                    msg='Input name.'
                    self.error_dialog.showMessage(msg)
                    raise Exception(msg)
                self.writeScoreDB()
                target= []
                for p in self.scoredb:
                    if p['Name'] ==self.nametbox.text():
                        target.append(p)
                self.scoredb=target
                self.showScoreDB(self.qlist.currentText())
                self.readScoreDB()

            elif sender.text()=="Inc":
                if len(self.nametbox.text()) ==0:
                    msg='Input name.'
                    self.error_dialog.showMessage(msg)
                    raise Exception(msg)
                if len(self.amounttbox.text()) ==0:
                    msg='Input amount.'
                    self.error_dialog.showMessage(msg)
                    raise Exception(msg)
                if not self.amounttbox.text().isdigit():
                    msg='Input the amount in integer form.'
                    self.error_dialog.showMessage(msg)
                    raise Exception(msg)
                for p in self.scoredb:
                    if p['Name'] ==self.nametbox.text():
                        p['Score'] += int(self.amounttbox.text())
                self.writeScoreDB()
                self.showScoreDB(self.qlist.currentText())

            elif sender.text()=="Show":
                self.showScoreDB(self.qlist.currentText())
        except  Exception as e:
             print('[Error]', e)

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

    def showScoreDB(self,key):
        self.resulttbox.clear()
        for p in sorted(self.scoredb, key=lambda person: person[key]):
            s = ""
            for attr in sorted(p):
                s += (attr+": "+str(p[attr])+"   ")
            self.resulttbox.append(str(s))
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
