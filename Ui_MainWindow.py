# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import time
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from data_rating import data_rating
from PyQt5.QtGui import QLinearGradient
from PyQt5.QtCore import QBasicTimer, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):  # 初始化函数
        # ---------------------窗口基本设置-----------------------
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 1090)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setWindowOpacity(7.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout.addWidget(self.textBrowser_3)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout.addWidget(self.textBrowser_4)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_3.addWidget(self.textBrowser)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(80, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionType_Here = QtWidgets.QAction(MainWindow)
        self.actionType_Here.setObjectName("actionType_Here")
        self.actionHello1 = QtWidgets.QAction(MainWindow)
        self.actionHello1.setObjectName("actionHello1")
        self.actionHello2 = QtWidgets.QAction(MainWindow)
        self.actionHello2.setObjectName("actionHello2")
        self.actiondakai = QtWidgets.QAction(MainWindow)
        self.actiondakai.setObjectName("actiondakai")
        self.actiondakai_2 = QtWidgets.QAction(MainWindow)
        self.actiondakai_2.setObjectName("actiondakai_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setWindowIcon(QIcon('./ico/编辑.ico'))
        self.statusBar()  # 设置一个状态栏
        self.setFocus()  # 设置一个焦点
        self.anim = None
        self.triggered = 0
        self.format = "csv"

        # ----------------------窗口基本设置-------------------------
        # ----------------------窗口附加设置-------------------------
        # 设置按键参数
        self.pushButton.setStyleSheet(
            "QPushButton{background-color:#CAE1FF}"  # 按键背景色
            "QPushButton:hover{color:#33CCFF}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:4px}"  # 圆角半径
            "QPushButton:pressed{background-color:#9FB6CD;border: None;}"  # 按下时的样式
        )

        # 设置文本框格式
        self.textBrowser.setStyleSheet(
            "QTextBrowser{border-radius:10px}"
            "QTextBrowser{background-color:#80ffffff}"
            "QTextBrowser{border-width:0}"
            "QTextBrowser{border-style:outset}"
        )

        self.textBrowser_3.setStyleSheet(
            "QTextBrowser{border-radius:5px}"
            "QTextBrowser{background-color:#80ffffff}"
            "QTextBrowser{border-width:0}"
            "QTextBrowser{border-style:outset}"
        )

        self.textBrowser_4.setStyleSheet(
            "QTextBrowser{border-radius:5px}"
            "QTextBrowser{background-color:#80ffffff}"
            "QTextBrowser{border-width:0}"
            "QTextBrowser{border-style:outset}"
        )

        self.pushButton_2.setStyleSheet(
            "QPushButton{background-color:#CAE1FF}"  # 按键背景色
            "QPushButton:hover{color:#33CCFF}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:4px}"  # 圆角半径
            "QPushButton:pressed{background-color:#9FB6CD;border: None;}"  # 按下时的样式
        )

        # 设置进度条样式
        self.progressBar.setStyleSheet(
            "QProgressBar { border: 2px solid grey; border-radius: 5px; background-color: #FFFFFF; text-align: center;}"
            "QProgressBar::chunk {background:QLinearGradient(x1:0,y1:0,x2:2,y2:0,stop:0 #fcfec3,stop:1  #fed775); }"
        )
        # 设置字体样式
        font = QFont()
        font.setBold(True)
        font.setWeight(30)
        self.progressBar.setFont(font)

        # 设置一个值表示进度条进度
        self.pv = 0
        self.progressBar.setValue(self.pv)
        self.progressBar.setFormat('Loaded  %v%'.format(self.progressBar.value() - self.progressBar.minimum()))
        # ----------------------窗口附加设置-------------------------
        # 输入数据文件
        open1 = QtWidgets.QAction(QIcon('./ico/搜索.ico'), u'打开', self)
        open1.setShortcut('Ctrl+O')
        open1.setStatusTip(u'打开数据文件')
        open1.triggered.connect(self.addData)

        datafile = self.menuBar()
        file1 = datafile.addMenu(u'数据')
        file1.addAction(open1)
        # 输入日志文件
        open2 = QtWidgets.QAction(QIcon('./ico/搜索.ico'), u'打开', self)
        open2.setShortcut('Ctrl+P')
        open2.setStatusTip(u'打开日志文件')
        open2.triggered.connect(self.addCondition)

        conditionfile = self.menuBar()
        file2 = conditionfile.addMenu(u'日志')
        file2.addAction(open2)

        # 输入存放文件的路径
        self.pushButton.clicked.connect(self.storePath)
        self.radioButton_2.setChecked(True)

        # 选择文件输出方式
        self.radioButton.toggled.connect(self.xlsOrDb)
        self.radioButton_2.toggled.connect(self.xlsOrDb)

        # 异常捕获
        try:
            # 确定操作
            self.pushButton_2.clicked.connect(self.rateData)
        except Exception as e:
            print('Reason:', e)

    # 给Widget赋值标题内容
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据标定"))
        self.pushButton.setText(_translate("MainWindow", "选择路径"))
        self.radioButton_2.setText(_translate("MainWindow", ".csv"))
        self.radioButton.setText(_translate("MainWindow", ".sqlite"))
        self.pushButton_2.setText(_translate("MainWindow", "确认"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionType_Here.setText(_translate("MainWindow", "Type Here"))
        self.actionHello1.setText(_translate("MainWindow", "Hello1"))
        self.actionHello2.setText(_translate("MainWindow", "Hello2"))
        self.actiondakai.setText(_translate("MainWindow", "打开    Ctrl+O"))
        self.actiondakai_2.setText(_translate("MainWindow", "打开    Ctrl+O"))

    # 绘制窗口背景图
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("./image/background.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    # 关闭窗口特效
    def closeEvent(self, event):
        # "退出"代表的是弹出框的标题,"你确认退出.."表示弹出框的内容
        if self.anim:
            return
        a = QMessageBox.question(self, '退出', '你确定要退出吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if a == QMessageBox.Yes:
            if self.anim == None:
                self.anim = QPropertyAnimation(self, b"windowOpacity")  # 设置动画对象
                self.anim.setDuration(1000)  # 设置动画时长
                self.anim.setStartValue(1)  # 设置初始属性，1.0为不透明
                self.anim.setEndValue(0)  # 设置结束属性，0为完全透明
                self.anim.finished.connect(self.close)  # 动画结束时，关闭窗口
                self.anim.start()  # 开始动画
                event.ignore()
        else:
            event.ignore()  # 忽略关闭事件

    # 加入数据文件
    def addData(self):
        files, filetype = QFileDialog.getOpenFileNames(self, "多文件选择", r"./", "All Files (*);;Text Files (*.csv)")
        # 清屏
        self.textBrowser_3.clear()
        # 将选择的文件名都打印到textBrowser控件中
        for file in files:
            self.textBrowser_3.append(file)

    # 加入日志文件
    def addCondition(self):
        files, filetype = QFileDialog.getOpenFileNames(self, "多文件选择", r"./", "All Files (*);;Text Files (*.csv)")
        # 清屏
        self.textBrowser_4.clear()
        # 将选择的文件名都打印到textBrowser控件中
        for file in files:
            self.textBrowser_4.append(file)

    # 加入存储路径
    def storePath(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", r"./")  # 起始路径
        self.textBrowser.setText(m)

    # 选择数据存储方式
    def xlsOrDb(self):
        if self.radioButton.isChecked():
            self.format = "db"
            if self.triggered == 0:
                text, ok = QInputDialog.getText(self, 'sqlite', '输入文件名称：')
                if ok:
                    self.db_name = text
                self.triggered = 1
        else:
            self.format = "csv"
            self.triggered = 0

    # 发送数据
    def sendData(self):
        excel_path = self.textBrowser_4.toPlainText()
        if len(self.textBrowser_3.toPlainText()):
            csv_paths = self.textBrowser_3.toPlainText().split("\n")
        else:
            csv_paths = []
        file_path = self.textBrowser.toPlainText()
        return excel_path, csv_paths, file_path

    # 标定数据
    def rateData(self):
        (excel_path, csv_paths, file_path) = self.sendData()
        if excel_path and csv_paths and file_path:
            self.pushButton_2.setEnabled(False)  # 将按钮设置为不可点击
            if self.format == "db":
                self.rd = RateDataThread(excel_path, csv_paths, file_path, self.db_name, self.format)  # 创建一个线程
            else:
                self.rd = RateDataThread(excel_path, csv_paths, file_path, None, self.format)  # 创建一个线程
            self.rd._process.connect(self.updatePro)  # 线程发过来的信号挂接到槽函数上
            self.rd.start()  # 线程启动
        elif len(csv_paths) == 0:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请选择数据文件')
            msg_box.exec_()
        elif not excel_path:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请选择日志文件')
            msg_box.exec_()
        elif not file_path:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请选择存储路径')
            msg_box.exec_()

    # 更新进度
    def updatePro(self, pro):
        self.pv = pro
        self.progressBar.setValue(float(self.pv))
        if (pro == 100):
            reply = QMessageBox.information(self, "提示信息", "数据转换成功。", QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)
            self.textBrowser.clear()
            self.textBrowser_3.clear()
            self.textBrowser_4.clear()
            self.pv = 0
            self.progressBar.setValue(self.pv)
            self.pushButton_2.setEnabled(True)  # 将按钮设置为可点击
            self.triggered = 0


# 用于标定数据耗时的操作
class RateDataThread(QThread):
    _process = pyqtSignal(float)
    _excel_path = ""
    _csv_paths = []
    _file_path = ""
    _file_name = ""
    _file_format = ""

    def __init__(self, excel_path, csv_paths, file_path, file_name, file_format):
        super(RateDataThread, self).__init__()
        self._excel_path = excel_path
        self._csv_paths = csv_paths
        self._file_path = file_path
        self._file_name = file_name
        self._file_format = file_format

    def run(self):
        per = len(self._csv_paths)
        cnt = 0
        for csv_path in self._csv_paths:
            if self._file_format == "csv":
                (filepath, filename) = os.path.split(csv_path)
                (name, suffix) = os.path.splitext(filename)
                self._file_name = name
            dr = data_rating(self._excel_path, csv_path, self._file_path, self._file_name, self._file_format)
            dr.handle_data()
            cnt += 1
            pro = round(float(cnt / per * 100), 2)
            self._process.emit(float(pro))
