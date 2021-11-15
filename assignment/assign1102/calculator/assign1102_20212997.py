# 박시윤-20212997
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from keypad import numPadList, operatorList
from constants import constantValues, constantList
from functions import functionList, functionMap


class Button(QToolButton):

    def __init__(self, text,callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parentheses = 0    #괄호 오류를 방지하기 위한 변수 parentheses
        self.resetList = ['0', 'Error!', '0으로 나눌 수 없습니다.']  #해당 문구가 계산기 출력란에 있을때 입력할 경우 없어질 것들

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()
        setting={
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList,'layout': funcLayout, 'columns': 1},
        }

        r = 0; c = 0;
        for label in setting.keys():
            r = 0; c = 0;
            buttonPad = setting[label]
            for i in buttonPad['buttons']:
                button = Button(i, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c=0; r+=1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            try:
                result = str(eval(self.display.text()))
            except ZeroDivisionError:
                result = "0으로 나눌 수 없습니다."

            except:
                result = "Error!"
            self.display.setText(result)

        elif key == 'C':
            self.parentheses = 0
            self.display.setText('0')


        elif key == '(':    #괄호 구현
            if (self.display.text()[-1].isnumeric() == True or self.display.text()[-1] == ')') and not(self.display.text() in self.resetList):   #마지막 글자가 숫자면 (를 썼을 때 *이 붙음.
                print(self.display.text()[-1])
                self.display.setText(self.display.text() + '*' + key)
            else:   #이외에는 그냥 붙음
                if self.display.text() in self.resetList:   #0과 오류들을 출력에서 없앰
                    self.display.setText('')
                self.display.setText(self.display.text() + key)
            self.parentheses += 1

        elif key == ')':    #괄호 구현
            if self.parentheses > 0:
                if self.display.text()[-1].isnumeric() == True: #마지막 글자가 숫자가 아니면 )를 못씀
                    self.display.setText(self.display.text() + key)
                    self.parentheses -= 1


        elif key in constantList:   #상수 구현
                if self.display.text()[-1] != ')':  # 괄호 구현
                    if self.display.text() in self.resetList:
                        self.display.setText('')
                else:  # 괄호 구현
                    if key.isnumeric() == True:
                        self.display.setText(self.display.text() + '*')
                self.display.setText(self.display.text() + constantValues[key])

        elif key in functionList:   #함수 구현
            n = self.display.text()
            value = functionMap[functionList.index(key)][1](n)
            self.display.setText((str(value)))


        else:   #일반 입력
            if self.display.text()[-1] != ')':  #마지막 글자가 )가 아니라면
                if self.display.text() in self.resetList:   #0이나 오류 등을 화면에서 없앰
                    self.display.setText('')
            else:   #마지막 글자가 )라면
                if key.isnumeric() == True:
                    self.display.setText(self.display.text() + '*')     #보통 괄호 다음에 아무것도 표기하지 않으면 곱하기이기 때문에 곱하기 추가
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

