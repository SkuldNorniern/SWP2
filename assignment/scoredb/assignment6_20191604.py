import pickle
import sys
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QApplication,
    QLabel,
    QComboBox,
    QTextEdit,
    QLineEdit,
)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = "assignment6.dat"
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB("Name")

    def initUI(self):
        self.lbl_Name = QLabel("Name: ", self)
        self.lbl_Age = QLabel("Age: ", self)
        self.lbl_Score = QLabel("Score: ", self)
        self.lbl_Amount = QLabel("Amount: ", self)
        self.lbl_Key = QLabel("Key: ", self)
        self.lbl_Result = QLabel("Result: ", self)

        self.line_Name = QLineEdit(self)
        self.line_Age = QLineEdit(self)
        self.line_Score = QLineEdit(self)
        self.line_Amount = QLineEdit(self)

        self.combo_Key = QComboBox(self)
        self.combo_Key.addItem("Name")
        self.combo_Key.addItem("Age")
        self.combo_Key.addItem("Score")

        self.button_Add = QPushButton("Add")
        self.button_Del = QPushButton("Del")
        self.button_Find = QPushButton("Find")
        self.button_Inc = QPushButton("Inc")
        self.button_Show = QPushButton("Show")

        self.button_Add.clicked.connect(self.addButton)
        self.button_Del.clicked.connect(self.delButton)
        self.button_Find.clicked.connect(self.findButton)
        self.button_Inc.clicked.connect(self.incButton)
        self.button_Show.clicked.connect(self.showButton)

        self.text_Result = QTextEdit(self)

        layout1 = QHBoxLayout()
        layout1.addWidget(self.lbl_Name)
        layout1.addWidget(self.line_Name)
        layout1.addWidget(self.lbl_Age)
        layout1.addWidget(self.line_Age)
        layout1.addWidget(self.lbl_Score)
        layout1.addWidget(self.line_Score)

        layout2 = QHBoxLayout()
        layout2.addStretch(1)
        layout2.addWidget(self.lbl_Amount)
        layout2.addWidget(self.line_Amount)
        layout2.addWidget(self.lbl_Key)
        layout2.addWidget(self.combo_Key)

        layout3 = QHBoxLayout()
        layout3.addStretch(1)
        layout3.addWidget(self.button_Add)
        layout3.addWidget(self.button_Del)
        layout3.addWidget(self.button_Find)
        layout3.addWidget(self.button_Inc)
        layout3.addWidget(self.button_Show)

        layout4 = QVBoxLayout()
        layout4.addWidget(self.lbl_Result)
        layout4.addWidget(self.text_Result)

        layout5 = QVBoxLayout()
        layout5.addLayout(layout1)
        layout5.addLayout(layout2)
        layout5.addLayout(layout3)
        layout5.addLayout(layout4)

        self.setLayout(layout5)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("Assignment6")
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, "rb")
        except FileNotFoundError as e:
            self.scoredb = []
            return self.scoredb

        try:
            self.scoredb = pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()
        return self.scoredb

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, "wb")
        pickle.dump(self.scoredb, fH)
        fH.close()

    def addButton(self):
        # if self.line_Name.text() == "" or self.line_Age.text() == "" or self.line_Score.text() == "":
        #   self.text_Result.setText("Check Input")
        record = {
            "Name": self.line_Name.text(),
            "Age": int(self.line_Age.text()),
            "Score": int(self.line_Score.text()),
        }
        self.scoredb += [record]
        self.showScoreDB("Name")

    def delButton(self):
        i = 0
        while i < len(self.scoredb):
            for p in self.scoredb:
                if p["Name"] == self.line_Name.text():
                    self.scoredb.remove(p)
            i += 1
        self.showScoreDB("Name")

    def findButton(self):
        temp_str = ""
        for p in self.scoredb:
            if p["Name"] == self.line_Name.text():
                count = 1
                for attr in sorted(p):
                    temp_str += attr + "=" + str(p[attr]) + "\t" * count
                    count += 1
                temp_str += "\n"
        self.text_Result.setText(temp_str)

    def incButton(self):
        for p in self.scoredb:
            if p["Name"] == self.line_Name.text():
                p["Score"] += int(self.line_Amount.text())
        self.showScoreDB("Name")

    def showButton(self):
        if self.combo_Key.currentText() == "Name":
            self.showScoreDB("Name")
        elif self.combo_Key.currentText() == "Age":
            self.showScoreDB("Age")
        else:
            self.showScoreDB("Score")
        # self.showScoreDB(self.combo_Key.currentText()) 한줄 코딩 가능

    def showScoreDB(self, keyname):
        temp_str = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            count = 1
            for attr in sorted(p):
                temp_str += attr + "=" + str(p[attr]) + "\t" * count
                count += 1
            temp_str += "\n"
        self.text_Result.setText(temp_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
