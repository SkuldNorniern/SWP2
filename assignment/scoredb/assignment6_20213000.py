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
        self.show()
        hbox = QHBoxLayout()
        Name = QLabel('Name')
        Age = QLabel('Age')
        Score = QLabel('Score')
        Amount = QLabel('Amount')

        NameEdit = QLineEdit()
        AgeEdit = QLineEdit()
        ScoreEdit = QLineEdit()
        AmountEdit = QLineEdit()


        h1box = QHBoxLayout()
        h1box.addStretch(1)
        h1box.addWidget(Name)
        h1box.addWidget(NameEdit)
        h1box.addWidget(Age)
        h1box.addWidget(AgeEdit)
        h1box.addWidget(Score)
        h1box.addWidget(ScoreEdit)

        h2box = QHBoxLayout()
        h2box.addStretch(1)
        h2box.addWidget(Amount)
        h2box.addWidget(AmountEdit)

        h3box = QHBoxLayout()
        addButton = QPushButton("Add", self)
        delButton = QPushButton("Del", self)
        findButton = QPushButton("Find", self)
        incButton = QPushButton("Inc", self)
        showButton = QPushButton("Show", self)
        addButton.clicked.connect(self.buttonClicked)
        delButton.clicked.connect(self.buttonClicked)
        findButton.clicked.connect(self.buttonClicked)
        incButton.clicked.connect(self.buttonClicked)
        showButton.clicked.connect(self.buttonClicked)
        h3box.addWidget(addButton)
        h3box.addWidget(delButton)
        h3box.addWidget(findButton)
        h3box.addWidget(incButton)
        h3box.addWidget(showButton)

        h4box = QHBoxLayout()
        result = QLabel('Result:')
        h4box.addWidget(result)

        h5box = QHBoxLayout()
        resultbox = QTextEdit()
        h5box.addWidget(resultbox)



        vBox = QVBoxLayout()
        vBox.addStretch(5)
        vBox.addLayout(h1box)
        vBox.addLayout(h2box)
        vBox.addLayout(h3box)
        vBox.addLayout(h4box)
        vBox.addLayout(h5box)




        self.setLayout(vBox)


    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')



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
        pass


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

