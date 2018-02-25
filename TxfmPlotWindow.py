# Window for plotting transform pairs

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from TxfmPlotHelper import TxfmPlotHelper

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as QMatFigCanvas
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as QMatNavToolbar
import matplotlib.pyplot as plt

# Class for the window
class TxfmPlotWindow (QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()

        self.initUI()

    # Initialize window & widgets
    def initUI(self):

        # Soft-coded stuffs
        frameStyle = QFrame.StyledPanel

        tph = TxfmPlotHelper()
        # Functions for performing the transforms
        def doTransform():
            self.statusBar().showMessage("Running")
            txfm = txfmSelBox.currentText()
            if (txfm == 'Z'):
                QMessageBox.warning(self, "Not Implemented", "Z-transform has not yet been implemented")
            else:
                try:
                    result = tph.Transform(tEdit.text(), txfm)
                except:
                    QMessageBox.critical(self, "Error", "Unable to transform " + tEdit.text())
                    result = tEdit.text(), 0
            # Deal with result
            self.statusBar().showMessage("Plotting")
            res_expr = result[1][0] if txfm == 'Laplace' else result
            sEdit.setText(str(res_expr))
            drawGraphs(result, txfm)
            self.statusBar().showMessage("Ready")

        def doInvTransform():
            self.statusBar().showMessage("Running")
            txfm = "Inv" + txfmSelBox.currentText()
            if (txfm == 'Z'):
                QMessageBox.warning(self, "Not Implemented", "Z-transform has not yet been implemented")
            else:
                try:
                    result = tph.Transform(sEdit.text(), txfm)
                except:
                    QMessageBox.critical(self, "Error", "Unable to transform " + sEdit.text())
                    result = sEdit.text(), 0
            # Deal with result
            self.statusBar().showMessage("Plotting")
            tEdit.setText(str(result[1]))
            drawGraphs(result, txfm)
            self.statusBar().showMessage("Ready")

        # Function for drawing the graphs based on current results
        def drawGraphs(results, txfm):
            # Helper to try calling plotter
            def tryPlot(canvas, expr, x):
                try:
                    p = tph.plot(expr, x)
                except:
                    QMessageBox.critical(self, "Error", "Unable to plot " + str(expr))
                    p = tph.plot("0", x)
                self.plot(canvas, p)

            if (txfm.startswith('Inv')): # Invert results
                sExpr, tExpr = results
            else:
                tExpr, sExpr = results
            if (txfm == 'Laplace'): # Cut out ROC info
                result_roc = sExpr[1:]
                sExpr = sExpr[0]
            # Plot tExpr
            tryPlot(sigCanvas, tExpr, 't')

            if (txfm.endswith('Laplace') or txfm.endswith('Z')):
                FtLabel.setText("ROC")
                # TODO draw pole-zero plot
            else: # Fourier
                FtLabel.setText("Fourier Transform")
                # Plot sExpr
                tryPlot(FtCanvas, sExpr, 's')

        #self.setCentralWidget(QWidget(self))

        QToolTip.setFont(QFont('SansSerif', 10))

        self.statusBar().showMessage("Ready")
        #### Menubar ####
        menubar = self.menuBar()
        # Menus
        fileMenu = menubar.addMenu('&File')

        # Items
        exitAct = QAction('E&xit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)

        # Matplotlib figures
        tFigure = plt.figure()
        sFigure = plt.figure()
        #self.plot(tFigure)
        #self.plot(sFigure)

        # Input labels
        tLabel = QLabel("Time Domain")
        sLabel = QLabel("S Domain")
        txfmLabel = QLabel("Transform")
        selLabel = QLabel("Select Transform")

        # Input widgets
        tEdit = QLineEdit() # Time domain
        sEdit = QLineEdit() # S domain
        #tEdit.textChanged[str].connect(sEdit.setText)
        t2sButton = QPushButton('⇓')
        t2sButton.clicked.connect(doTransform)
        tEdit.returnPressed.connect(doTransform)
        s2tButton = QPushButton('⇑')
        s2tButton.clicked.connect(doInvTransform)
        sEdit.returnPressed.connect(doInvTransform)
        txfmSelBox = QComboBox()
        txfmSelBox.addItems(['Laplace', 'Fourier', 'Z'])

        # Output labels
        sigLabel = QLabel("Signal")
        FtLabel = QLabel("Transform")
        propLabel = QLabel("Properties")

        # Output widgets
        sigCanvas = QMatFigCanvas(tFigure)
        FtCanvas = QMatFigCanvas(sFigure)
        rocLabel = QLabel("ROC: N/A")
        stableLabel = QLabel("Stable: N/A")
        causalLabel = QLabel("Causal: N/A")

        # Layout
        LRSplitter = QSplitter(Qt.Horizontal)
        
        # Left Column
        gridL = QGridLayout()
        LFrame = QFrame()
        LFrame.setLayout(gridL)
        LFrame.setFrameShape(frameStyle)
        LRSplitter.addWidget(LFrame)

        # Right Column
        outSplitter = QSplitter(Qt.Vertical)
        outSplitter.setFrameShape(frameStyle)
        RFrame = QFrame()
        #RFrame.setLayout(gridR)
        sigFrame = QFrame()
        sigGrid = QGridLayout()
        sigFrame.setLayout(sigGrid)
        sigFrame.setFrameShape(frameStyle)
        FtFrame = QFrame()
        FtGrid = QGridLayout()
        FtFrame.setLayout(FtGrid)
        outSplitter.addWidget(sigFrame)
        outSplitter.addWidget(FtFrame)
        LRSplitter.addWidget(outSplitter)

        # Upper left
        gridL.addWidget(tLabel, 0, 0)
        gridL.addWidget(tEdit, 0, 1, 1, 2)
        gridL.addWidget(txfmLabel, 1, 0)
        gridL.addWidget(t2sButton, 1, 1)
        gridL.addWidget(s2tButton, 1, 2)
        gridL.addWidget(sLabel, 2, 0)
        gridL.addWidget(sEdit, 2, 1, 1, 2)
        gridL.addWidget(selLabel, 3, 0)
        gridL.addWidget(txfmSelBox, 3, 1, 1, 2)

        # Lower left
        gridL.addWidget(QWidget(), 4, 0) # For spacing
        gridL.setRowStretch(4,1)
        gridL.addWidget(propLabel, 5, 0, 1, 3)
        gridL.addWidget(rocLabel, 6, 0, 1, 3)
        gridL.addWidget(stableLabel, 7, 0, 1, 3)
        gridL.addWidget(causalLabel, 8, 0, 1, 3)

        # Uppder Right
        sigGrid.addWidget(sigLabel, 0, 0)
        sigGrid.addWidget(sigCanvas, 1, 0, 3, 1)

        # Lower Right
        FtGrid.addWidget(FtLabel, 4, 0)
        FtGrid.addWidget(FtCanvas, 5, 0, 3, 1)

        self.setCentralWidget(LRSplitter)

        # Window setup
        #self.centralWidget().setLayout(grid)
        #self.move(300, 300)
        #self.resize(300, 220)
        self.setWindowTitle("Transform Pair Plotter")
        #self.setWindowIcon(QIcon("icon.png"))
        self.show()

    def plot(self, canvas, symplot):
            # Helper func from https://stackoverflow.com/questions/46810880/display-two-sympy-plots-as-two-matplotlib-subplots
            def move_symplot_to_axes(p, ax):
                backend = p.backend(p)
                backend.ax = ax
                backend.process_series()
                backend.ax.spines['right'].set_color('none')
                backend.ax.spines['bottom'].set_position('zero')
                backend.ax.spines['top'].set_color('none')
                plt.close(backend.fig)

            figure = canvas.figure

            # instead of ax.hold(False)
            figure.clear()

            # create an axis
            ax = figure.add_subplot(111)

            # move data to plot
            move_symplot_to_axes(symplot, ax)
            #ax.plot(data, '*-')

            # refresh canvas
            canvas.draw()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = TxfmPlotWindow()
    sys.exit(app.exec_())
