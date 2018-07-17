# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'noise_mease.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import visa
import time
import numpy as np
import pyqtgraph as pg
pg.setConfigOption('background', 'w')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 550)
        MainWindow.setMinimumSize(QtCore.QSize(650, 550))
        MainWindow.setMaximumSize(QtCore.QSize(650, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mx_pwr = QtWidgets.QLabel(self.centralwidget)
        self.mx_pwr.setMinimumSize(QtCore.QSize(100, 20))
        self.mx_pwr.setMaximumSize(QtCore.QSize(100, 20))
        self.mx_pwr.setObjectName("mx_pwr")
        self.gridLayout_3.addWidget(self.mx_pwr, 0, 2, 1, 1)
        self.Meas_time = QtWidgets.QLabel(self.centralwidget)
        self.Meas_time.setMinimumSize(QtCore.QSize(105, 20))
        self.Meas_time.setMaximumSize(QtCore.QSize(105, 20))
        self.Meas_time.setObjectName("Meas_time")
        self.gridLayout_3.addWidget(self.Meas_time, 3, 1, 1, 1)
        self.IDN = QtWidgets.QLabel(self.centralwidget)
        self.IDN.setMinimumSize(QtCore.QSize(100, 20))
        self.IDN.setMaximumSize(QtCore.QSize(100, 20))
        self.IDN.setObjectName("IDN")
        self.gridLayout_3.addWidget(self.IDN, 0, 0, 1, 1)
        self.TIME = QtWidgets.QTextEdit(self.centralwidget)
        self.TIME.setMinimumSize(QtCore.QSize(110, 30))
        self.TIME.setMaximumSize(QtCore.QSize(110, 30))
        self.TIME.setObjectName("TIME")
        self.gridLayout_3.addWidget(self.TIME, 4, 1, 1, 1)
        self.IDN_dsip = QtWidgets.QTextBrowser(self.centralwidget)
        self.IDN_dsip.setMinimumSize(QtCore.QSize(220, 30))
        self.IDN_dsip.setMaximumSize(QtCore.QSize(220, 30))
        self.IDN_dsip.setObjectName("IDN_dsip")
        self.gridLayout_3.addWidget(self.IDN_dsip, 1, 0, 1, 2)
        self.AVG = QtWidgets.QTextEdit(self.centralwidget)
        self.AVG.setMinimumSize(QtCore.QSize(110, 30))
        self.AVG.setMaximumSize(QtCore.QSize(110, 30))
        self.AVG.setObjectName("AVG")
        self.gridLayout_3.addWidget(self.AVG, 4, 0, 1, 1)
        self.Plot = PlotWidget(self.centralwidget)
        self.Plot.setMinimumSize(QtCore.QSize(590, 320))
        self.Plot.setMaximumSize(QtCore.QSize(590, 320))
        self.Plot.setObjectName("Plot")
        self.gridLayout_3.addWidget(self.Plot, 2, 0, 1, 5)
        self.samplingpoint = QtWidgets.QTextBrowser(self.centralwidget)
        self.samplingpoint.setMinimumSize(QtCore.QSize(110, 30))
        self.samplingpoint.setMaximumSize(QtCore.QSize(110, 30))
        self.samplingpoint.setObjectName("samplingpoint")
        self.gridLayout_3.addWidget(self.samplingpoint, 4, 2, 1, 1)
        self.num_repeat = QtWidgets.QLabel(self.centralwidget)
        self.num_repeat.setMinimumSize(QtCore.QSize(100, 20))
        self.num_repeat.setMaximumSize(QtCore.QSize(100, 20))
        self.num_repeat.setObjectName("num_repeat")
        self.gridLayout_3.addWidget(self.num_repeat, 3, 3, 1, 1)
        self.smpl_pint = QtWidgets.QLabel(self.centralwidget)
        self.smpl_pint.setMinimumSize(QtCore.QSize(100, 20))
        self.smpl_pint.setMaximumSize(QtCore.QSize(100, 20))
        self.smpl_pint.setObjectName("smpl_pint")
        self.gridLayout_3.addWidget(self.smpl_pint, 3, 2, 1, 1)
        self.Num_of_repeats = QtWidgets.QTextBrowser(self.centralwidget)
        self.Num_of_repeats.setMinimumSize(QtCore.QSize(110, 30))
        self.Num_of_repeats.setMaximumSize(QtCore.QSize(110, 30))
        self.Num_of_repeats.setObjectName("Num_of_repeats")
        self.gridLayout_3.addWidget(self.Num_of_repeats, 4, 3, 1, 1)
        self.Noise = QtWidgets.QPushButton(self.centralwidget)
        self.Noise.setMinimumSize(QtCore.QSize(110, 30))
        self.Noise.setMaximumSize(QtCore.QSize(110, 30))
        self.Noise.setObjectName("Noise")
        self.gridLayout_3.addWidget(self.Noise, 4, 4, 1, 1)
        self.Avg_time = QtWidgets.QLabel(self.centralwidget)
        self.Avg_time.setMinimumSize(QtCore.QSize(100, 20))
        self.Avg_time.setMaximumSize(QtCore.QSize(100, 20))
        self.Avg_time.setObjectName("Avg_time")
        self.gridLayout_3.addWidget(self.Avg_time, 3, 0, 1, 1)
        self.mx_pwr_disp = QtWidgets.QTextBrowser(self.centralwidget)
        self.mx_pwr_disp.setMinimumSize(QtCore.QSize(110, 30))
        self.mx_pwr_disp.setMaximumSize(QtCore.QSize(110, 30))
        self.mx_pwr_disp.setObjectName("mx_pwr_disp")
        self.gridLayout_3.addWidget(self.mx_pwr_disp, 1, 2, 1, 1)
        self.pwr_drft_disp = QtWidgets.QTextBrowser(self.centralwidget)
        self.pwr_drft_disp.setMinimumSize(QtCore.QSize(110, 30))
        self.pwr_drft_disp.setMaximumSize(QtCore.QSize(110, 30))
        self.pwr_drft_disp.setObjectName("pwr_drft_disp")
        self.gridLayout_3.addWidget(self.pwr_drft_disp, 1, 3, 1, 1)
        self.pwr_drft = QtWidgets.QLabel(self.centralwidget)
        self.pwr_drft.setMinimumSize(QtCore.QSize(100, 20))
        self.pwr_drft.setMaximumSize(QtCore.QSize(100, 20))
        self.pwr_drft.setObjectName("pwr_drft")
        self.gridLayout_3.addWidget(self.pwr_drft, 0, 3, 1, 1)
        self.noise_p2p = QtWidgets.QLabel(self.centralwidget)
        self.noise_p2p.setMinimumSize(QtCore.QSize(100, 20))
        self.noise_p2p.setMaximumSize(QtCore.QSize(100, 20))
        self.noise_p2p.setObjectName("noise_p2p")
        self.gridLayout_3.addWidget(self.noise_p2p, 0, 4, 1, 1)
        self.noise_p2p_disp = QtWidgets.QTextBrowser(self.centralwidget)
        self.noise_p2p_disp.setMinimumSize(QtCore.QSize(110, 30))
        self.noise_p2p_disp.setMaximumSize(QtCore.QSize(110, 30))
        self.noise_p2p_disp.setObjectName("noise_p2p_disp")
        self.gridLayout_3.addWidget(self.noise_p2p_disp, 1, 4, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 120)
        self.gridLayout_3.setColumnStretch(1, 120)
        self.gridLayout_3.setColumnStretch(2, 120)
        self.gridLayout_3.setColumnStretch(3, 120)
        self.gridLayout_3.setColumnStretch(4, 120)
        self.gridLayout_3.setRowStretch(0, 50)
        self.gridLayout_3.setRowStretch(1, 30)
        self.gridLayout_3.setRowStretch(2, 340)
        self.gridLayout_3.setRowStretch(3, 50)
        self.gridLayout_3.setRowStretch(4, 30)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.Noise.clicked.connect(self.Meas)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mx_pwr.setText(_translate("MainWindow", "Max Power (dBm)"))
        self.Meas_time.setText(_translate("MainWindow", "Measurement time (s)"))
        self.IDN.setText(_translate("MainWindow", "Tool IDN"))
        self.num_repeat.setText(_translate("MainWindow", "Number of repeats"))
        self.smpl_pint.setText(_translate("MainWindow", "Sampling points"))
        self.Noise.setText(_translate("MainWindow", "NOISE"))
        self.Avg_time.setText(_translate("MainWindow", "Averaging time (us)"))
        self.pwr_drft.setText(_translate("MainWindow", "Power Drift (dB)"))
        self.noise_p2p.setText(_translate("MainWindow", "Noise P-P (dBm)"))

    
    def Meas(self):
        rm = visa.ResourceManager()
        MPM = rm.open_resource('GPIB0::16::INSTR')
        self.IDN_dsip.setText(MPM.query("*IDN?"))
        Avg = float(self.AVG.toPlainText())
        Meas_time = float(self.TIME.toPlainText())
        Numofrepeats=1
        samplingpoints=int(Meas_time)*1000/int(Avg)
        self.samplingpoint.setText(str(samplingpoints))
        Numofrepeats=1
        if samplingpoints>1000000:
            Numofrepeats=samplingpoints/1000000
        self.Num_of_repeats.setText(str(Numofrepeats))
        loop=1
        while loop<Numofrepeats+1:
            MPM.write("ZERO")
            time.sleep(3)
            MPM.write("WAV 1310")
            MPM.write("UNIT 0")
            MPM.write("TRIG 0")
            MPM.write("WMOD FREERUN")
            MPM.write("LOGN "+str(samplingpoints))
            MPM.write("AVG "+str(Avg))
            check=[]
            rawdata=[]
            for i in range (1,2):
                MPM.write("LEV "+str(i))
                time.sleep(0.5)
                MPM.write("MEAS")
        
                check=MPM.query("STAT?").split(',')
                while True:
                    check=MPM.query("STAT?").split(',')
                    if check[0]=='0':
                        time.sleep (0.1)
                    else:
                        break
                rawdata=MPM.query_binary_values("LOGG? 0,1",'f')
                x=np.arange(1,len(rawdata)+1)
#                k,= plt.plot(x,rawdata)
            
                yfit = []
            
                z=np.polyfit(x,rawdata,2)
                for i in x:
                    yfit.append(z[0]*i**2+z[1]*i+z[2])
            
                diff=[]
                for i in range(len(rawdata)):
                    diff.append(rawdata[i]-yfit[i])
        self.Plot.plot(x,rawdata, clear=True)
        self.mx_pwr_disp.setText(str(max(yfit)))
        self.pwr_drft_disp.setText(str(max(diff)-min(diff)))
        self.noise_p2p_disp.setText(str(np.std(diff)*2))

if __name__ == "__main__":
    import sys
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

