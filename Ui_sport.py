# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\code\assign\chinese\c++python\SportsInfo\sport.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1441, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 110, 1351, 741))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 20, 71, 31))
        self.label_2.setObjectName("label_2")
        self.leaguename = QtWidgets.QLineEdit(self.centralwidget)
        self.leaguename.setGeometry(QtCore.QRect(510, 30, 121, 21))
        self.leaguename.setObjectName("leaguename")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(670, 30, 71, 31))
        self.label_3.setObjectName("label_3")
        self.newtitle = QtWidgets.QLineEdit(self.centralwidget)
        self.newtitle.setGeometry(QtCore.QRect(730, 40, 121, 21))
        self.newtitle.setObjectName("newtitle")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 81, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 70, 121, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.querydata = QtWidgets.QPushButton(self.centralwidget)
        self.querydata.setGeometry(QtCore.QRect(350, 70, 91, 31))
        self.querydata.setObjectName("querydata")
        self.exportdata = QtWidgets.QPushButton(self.centralwidget)
        self.exportdata.setGeometry(QtCore.QRect(870, 70, 91, 31))
        self.exportdata.setObjectName("exportdata")
        self.fromDateTime = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.fromDateTime.setGeometry(QtCore.QRect(100, 20, 141, 22))
        self.fromDateTime.setObjectName("fromDateTime")
        self.toDateTime = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.toDateTime.setGeometry(QtCore.QRect(290, 20, 141, 22))
        self.toDateTime.setObjectName("toDateTime")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 20, 71, 31))
        self.label_5.setObjectName("label_5")
        self.savepath = QtWidgets.QLineEdit(self.centralwidget)
        self.savepath.setGeometry(QtCore.QRect(520, 70, 291, 31))
        self.savepath.setObjectName("savepath")
        self.pathselect = QtWidgets.QPushButton(self.centralwidget)
        self.pathselect.setGeometry(QtCore.QRect(820, 73, 31, 31))
        self.pathselect.setObjectName("pathselect")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1441, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "联赛名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "主队名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "客队名"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "主赔率"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "主盘口"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "客赔率"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "客盘口"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "全场比分"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "指数运算结果"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "新闻首发时间"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "新闻主标题"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "新闻内容"))
        self.label.setText(_translate("MainWindow", "开赛时间:"))
        self.label_2.setText(_translate("MainWindow", "联赛名:"))
        self.label_3.setText(_translate("MainWindow", "新闻标题:"))
        self.label_4.setText(_translate("MainWindow", "指数运算结果:"))
        self.querydata.setText(_translate("MainWindow", "查询"))
        self.exportdata.setText(_translate("MainWindow", "导出"))
        self.label_5.setText(_translate("MainWindow", "到"))
        self.pathselect.setText(_translate("MainWindow", "..."))
