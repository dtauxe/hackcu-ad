#!/usr/bin/python3

import sys
from TxfmPlotWindow import TxfmPlotWindow
from PyQt5.QtWidgets import QApplication

## MAIN
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TxfmPlotWindow()
    sys.exit(app.exec_())
