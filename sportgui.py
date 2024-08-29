
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import QLineEdit, QApplication, QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Ui_sport import Ui_MainWindow
# from myVideoWidget import myVideoWidget
import sys
# from services.sport.sportquery
from PyQt5 import QtCore, QtGui, QtWidgets
from dao import sportinfo
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTimeEdit, QVBoxLayout, QWidget

class sportMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.querydata.clicked.connect(self.querysportinfo)   # 打开视频文件按钮
        arroddsdata = sportinfo.query_odds_data()

        # self.lineTimeInfo.clicked.connect(self.show_time_dialog)   # 打开视频文件按钮
        # self.lineTimeInfo.setPlaceholderText("Click Please")

        # self.lineTimeInfo.mousePressEvent = self.show_time_dialog
        self.dateTimeEdit.setCalendarPopup(True)
        
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        # # 设置最小日期
        # self.dateTimeEdit.setMinimumDate(QDate.currentDate().addDays(-365))
        # # 设置最大日期
        # self.dateTimeEdit.setMaximumDate(QDate.currentDate().addDays(365))
        # # 允许弹出日历控件
        
          # 设置时间部分可见
        # self.dateTimeEdit.setTimeSpec(Qt.TimeSpec.TimeSpec_Second)

        # self.dateTimeEdit.dateChanged.connect(self.onDateChanged)
        # self.dateTimeEdit.dateTimeChanged.connect(self.onDateTimeChanged)
        # self.dateTimeEdit.timeChanged.connect(self.onTimeChanged)

        for i in range(len(arroddsdata)):
            self.tableWidget.insertRow(i)
            item = QtWidgets.QTableWidgetItem(str(arroddsdata[i]['start_time']))
            self.tableWidget.setItem(i, 0, item)

            item = QtWidgets.QTableWidgetItem(arroddsdata[i]['eventname'])
            self.tableWidget.setItem(i, 1, item)

            item = QtWidgets.QTableWidgetItem(arroddsdata[i]['HomeName'])
            self.tableWidget.setItem(i, 2, item)

            item = QtWidgets.QTableWidgetItem(arroddsdata[i]['AwayName'])
            self.tableWidget.setItem(i, 3, item)

            item = QtWidgets.QTableWidgetItem(arroddsdata[i]['HandicapHomehcapdisp'])
            self.tableWidget.setItem(i, 4, item)

            item = QtWidgets.QTableWidgetItem(arroddsdata[i]['HandicapHomeRate'])
            self.tableWidget.setItem(i, 5, item)

            item = QtWidgets.QTableWidgetItem(arroddsdata[i]['Handicapawayhcapdisp'])
            self.tableWidget.setItem(i, 6, item)

            item = QtWidgets.QTableWidgetItem(arroddsdata[i]['HandicapawayRate'])
            self.tableWidget.setItem(i, 7, item)

            item = QtWidgets.QTableWidgetItem(arroddsdata[i]['currentscore'])
            self.tableWidget.setItem(i, 8, item)
        # for i in range(12):
        #     self.tableWidget.insertRow(i)
        #     for j in range(12):
                
        #         item = QtWidgets.QTableWidgetItem("111222fffbbb"+str(i))
        #         self.tableWidget.setItem(i, j, item)
        # self.sld_video_pressed=False  #判断当前进度条识别否被鼠标点击
            
    def show_time_dialog(self, mouseEvent):
        time_edit, _ = QTimeEdit.getTime(self, "选择时间", Qt.currentDateTime())
        self.lineTimeInfo.setPlaceholderText("Thanks Man :)")
        print(time_edit.time())

     # 日期发生改变时执行
    def onDateChanged(self, date):
        print(date)
 
    # 无论日期还是时间发生改变，都会执行
    def onDateTimeChanged(self, dateTime):
        print(dateTime)
 
    # 时间发生改变时执行
    def onTimeChanged(self, time):
        print(time)

    def querysportinfo(self):
        print("testttt")
        odds_data = sportinfo.query_odds_data()
        for data in odds_data:
            print("data=", data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = sportMainWindow()
    vieo_gui.show()
    sys.exit(app.exec_())


