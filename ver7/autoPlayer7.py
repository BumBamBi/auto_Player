import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtTest
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets


################## 여기 설정해주세요################
# 틀고 싶은 과목 영어명 일부
CLASS_NAME = 'IMAGE'
# 틀고싶은 영상 주차 범위
START_SECTION = 2
END_SECTION = 15
# 한 주차내에 영상 파일 위에 몇개의 파일이 있는가(최대)
OTHERS_CNT = 2
ID = ''
PW = ''
###############################################
# 기본 변수
video_index = 1
section_now = START_SECTION
###############################################

###############################################
# driver import
if  getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path)
else:
    # Chrome 웹 드라이버 생성
    driver = webdriver.Chrome('./chromedriver')
###############################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 496)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.name.setObjectName("name")
        self.notice = QtWidgets.QLabel(self.centralwidget)
        self.notice.setGeometry(QtCore.QRect(410, 50, 261, 31))
        self.notice.setObjectName("notice")
        self.start = QtWidgets.QLabel(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(20, 110, 171, 21))
        self.start.setObjectName("start")
        self.end = QtWidgets.QLabel(self.centralwidget)
        self.end.setGeometry(QtCore.QRect(20, 180, 171, 21))
        self.end.setObjectName("end")
        self.others = QtWidgets.QLabel(self.centralwidget)
        self.others.setGeometry(QtCore.QRect(20, 250, 341, 21))
        self.others.setObjectName("others")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 20, 161, 31))
        self.label_6.setObjectName("label_6")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(110, 280, 341, 191))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.btn_go = QtWidgets.QPushButton(self.centralwidget)
        self.btn_go.setGeometry(QtCore.QRect(550, 360, 121, 81))
        self.btn_go.setObjectName("btn_go")
        self.txt_name = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(150, 20, 131, 31))
        self.txt_name.setDocumentTitle("")
        self.txt_name.setObjectName("txt_name")
        self.txt_end = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_end.setGeometry(QtCore.QRect(190, 170, 131, 31))
        self.txt_end.setObjectName("txt_end")
        self.txt_others = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_others.setGeometry(QtCore.QRect(360, 240, 131, 31))
        self.txt_others.setObjectName("txt_others")
        self.txt_start = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_start.setGeometry(QtCore.QRect(190, 100, 131, 31))
        self.txt_start.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txt_start.setObjectName("txt_start")
        self.txt_id = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_id.setGeometry(QtCore.QRect(510, 100, 131, 31))
        self.txt_id.setDocumentTitle("")
        self.txt_id.setObjectName("txt_id")
        self.name_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_2.setGeometry(QtCore.QRect(470, 100, 31, 31))
        self.name_2.setObjectName("name_2")
        self.name_3 = QtWidgets.QLabel(self.centralwidget)
        self.name_3.setGeometry(QtCore.QRect(460, 140, 31, 31))
        self.name_3.setObjectName("name_3")
        self.txt_pw = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_pw.setGeometry(QtCore.QRect(510, 140, 131, 31))
        self.txt_pw.setDocumentTitle("")
        self.txt_pw.setObjectName("txt_pw")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_go.clicked.connect(self.go)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "과목명  :"))
        self.notice.setText(_translate("MainWindow", "(우상단의 Englich(en)으로 변경 후 확인)"))
        self.start.setText(_translate("MainWindow", "틀고싶은 영상 주차 시작 :"))
        self.end.setText(_translate("MainWindow", "틀고싶은 영상 주차 끝 :"))
        self.others.setText(_translate("MainWindow", "한 주차 내에서 영상파일 위에 있는 파일 개수(최대) :"))
        self.label_6.setText(_translate("MainWindow", "사이트가 영어면 영어"))
        self.btn_go.setText(_translate("MainWindow", "do macro"))
        self.name_2.setText(_translate("MainWindow", "ID :"))
        self.name_3.setText(_translate("MainWindow", "PW :"))

    def go(self):
        global CLASS_NAME
        global OTHERS_CNT
        global START_SECTION
        global END_SECTION
        global video_index
        global section_now
        global ID
        global PW

        CLASS_NAME = str(self.txt_name.toPlainText())
        START_SECTION = int(str(self.txt_start.toPlainText()))
        END_SECTION = int(str(self.txt_end.toPlainText()))
        OTHERS_CNT = int(str(self.txt_others.toPlainText()))
        ID = str(self.txt_id.toPlainText())
        PW = str(self.txt_pw.toPlainText())

        url = "http://cyber.inu.ac.kr/"

        # url 로딩
        driver.get(url)

        # 로그인 정보
        driver_id = driver.find_element_by_id("input-username")
        driver_id.send_keys(ID)  # 문자열 형식으로 아이디 입력

        driver_pw = driver.find_element_by_id('input-password')
        driver_pw.send_keys(PW)  # 문자열 형식으로 비밀번호 입력

        # 로그인 버튼 클릭
        login = driver.find_element_by_class_name("btn-success")
        login.click()
        # enter
        # driver_pw.send_keys(Keys.ENTER)

        close_notice = driver.find_element_by_xpath('//*[@id="notice_popup_1_276202"]/div[3]/span').click()

        go_class = driver.find_element_by_partial_link_text(CLASS_NAME)
        go_class.click()

        while 1:
            if int(section_now) > END_SECTION:
                break
            try:
                # set time
                print('start - ', video_index)
                timeline = driver.find_element_by_xpath(
                    '//*[@id="section-' + str(section_now) + '"]/div[3]/ul/li[' + str(
                        video_index) + ']/div/div/div[2]/div/span/span[2]').text
                timeline = timeline.replace(", ", "")
                print('time : ', timeline)

                # click and open video
                go_video_site = driver.find_element_by_xpath(
                    '//*[@id="section-' + str(section_now) + '"]/div[3]/ul/li[' + str(
                        video_index) + ']/div/div/div[2]/div/a').click()
                print('open video')

                # change tab
                driver.switch_to_window(driver.window_handles[1])

                # play video
                try:
                    # not yet played video
                    start = driver.find_element_by_xpath('//*[@id="vod_viewer"]').click()
                except:
                    # already played
                    alert = driver.switch_to.alert
                    alert.accept()

                # wait playing video
                time.sleep(3)
                time.sleep(int(timeline[:2]) * 60 + int(timeline[3:]))
                time.sleep(3)

                # close and change tab
                driver.close()
                driver.switch_to_window(driver.window_handles[0])
                time.sleep(3)

                # set var
                video_index += 1
            except:
                if video_index > OTHERS_CNT:
                    section_now += 1
                    video_index = 1
                else:
                    video_index += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

