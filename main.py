from PyQt4 import QtCore, QtGui
from qalq import Ui_MainWindow
import operator
import sys

class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect(self.ui.buttonBye,    QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))
        self.connect(self.ui.buttonPlus,   QtCore.SIGNAL('clicked()'), self.show_sum)
        self.connect(self.ui.buttonMinus,  QtCore.SIGNAL('clicked()'), self.show_difference)
        self.connect(self.ui.buttonTimes,  QtCore.SIGNAL('clicked()'), self.show_product)
        self.connect(self.ui.buttonDivide, QtCore.SIGNAL('clicked()'), self.show_quotient)

    def get_first(self):
        return self._get_value(0)

    def get_second(self):
        return self._get_value(1)

    def show_sum(self):
        self._show_result(operator.add)

    def show_difference(self):
        self._show_result(operator.sub)

    def show_product(self):
        self._show_result(operator.mul)

    def show_quotient(self):
        if self.get_second() != 0:
            self._show_result(operator.div)
        else:
            self._show_error()

    def _get_value(self, index):
        inputs = [self.ui.inputFirst, self.ui.inputSecond]
        try:
            x = float(inputs[index].text())
        except ValueError:
            x = None
        return x

    def _show_result(self, op):
        x, y = self.get_first(), self.get_second()
        if x is None or y is None:
            t = ''
        else:
            t = '{:g}'.format(op(x, y))
        self.ui.labelResult.setText(t)

    def _show_error(self, msg='Error'):
        self.ui.labelResult.setText(msg)


def main():
    app = QtGui.QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
