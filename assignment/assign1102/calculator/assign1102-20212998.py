from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
    QLineEdit, QToolButton, QSizePolicy, QLayout, QGridLayout)


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

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        for i in self.digitButton:
            self.digitButton[i] = Button(str(i), self.btnCli)

        # . and = Buttons
        self.decButton = Button('.', self.btnCli)
        self.eqButton = Button('=', self.btnCli)

        # Operator Buttons
        self.mulButton = Button('*', self.btnCli)
        self.divButton = Button('/', self.btnCli)
        self.addButton = Button('+', self.btnCli)
        self.subButton = Button('-', self.btnCli)

        # Parentheses Buttons
        self.lparButton = Button('(', self.btnCli)
        self.rparButton = Button(')', self.btnCli)

        # Clear Button
        self.clearButton = Button('C', self.btnCli)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        numLayout.addWidget(self.digitButton[0], 3, 0)
        for i in range(1,10):
            numLayout.addWidget(self.digitButton[i], 2-(i-1)//3, (i-1)%3)

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def btnCli(self):
            button = self.sender()
            key = button.text()

            if key == '=':
                result = str(eval(self.display.text()))
                self.display.setText(result)
            elif key == 'C':
                self.display.setText('0')
            else:
                if self.display.text()[0] == '0':
                    self.display.setText('')
                self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())