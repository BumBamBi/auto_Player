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
# 틀고 싶은 과목명 일부
CLASS_NAME = ['', '', '', '']
# 틀고싶은 영상 주차 범위
START_SECTION = 2
END_SECTION = 15
# 한 주차내에 영상 파일 위에 몇개의 파일이 있는가(최대)
OTHERS_CNT = 10
ID = ''
PW = ''
###############################################
# 기본 변수
video_index = 1
section_now = START_SECTION
###############################################

###############################################
# driver import
if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path)
else:
    # Chrome 웹 드라이버 생성
    driver = webdriver.Chrome('./chromedriver')


###############################################


## if gui in .py, then delete
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


form = resource_path('Player_gui.ui')
form_class = uic.loadUiType(form)[0]


###############################################################


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.txt_name_1.setText('IMAGE')

        self.txt_start.setText('1')
        self.txt_end.setText('2')

        self.btn_go.clicked.connect(self.go)

    def go(self):
        global CLASS_NAME
        global OTHERS_CNT
        global START_SECTION
        global END_SECTION
        global video_index
        global section_now
        global ID
        global PW

        CLASS_NAME[0] = str(self.txt_name_1.toPlainText())
        CLASS_NAME[1] = str(self.txt_name_2.toPlainText())
        CLASS_NAME[2] = str(self.txt_name_3.toPlainText())
        CLASS_NAME[3] = str(self.txt_name_4.toPlainText())
        START_SECTION = int(self.txt_start.toPlainText())
        END_SECTION = int(self.txt_end.toPlainText())
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

        try:
            # pop up
            close_notice = driver.find_element_by_xpath('//*[@id="notice_popup_1_276202"]/div[3]/span').click()
        except:
            print('non popup')

        for i in [0, 1, 2, 3]:
            if not CLASS_NAME[i] == '':
                try:
                    go_class = driver.find_element_by_partial_link_text(CLASS_NAME[i]).click()
                except:
                    print('ERROR! do not same class name!')
                    driver.quit()
                    return

                while 1:
                    if section_now > END_SECTION:
                        # reach END_SECTION -> home back
                        go_top = driver.find_element_by_xpath('//*[@id="back-top"]').click()
                        time.sleep(3)
                        homeback = driver.find_element_by_xpath('//*[@id="page-header"]/nav/div/div[1]/a').click()
                        CLASS_NAME[i] = ''
                        section_now = START_SECTION
                        video_index = 1
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
                        time.sleep(5)
                        time.sleep(int(timeline[:2]) * 60 + int(timeline[3:]))
                        time.sleep(5)

                        # close and change tab
                        driver.close()
                        driver.switch_to_window(driver.window_handles[0])
                        time.sleep(2)

                        # set var
                        video_index += 1
                    except:
                        if video_index > OTHERS_CNT:
                            section_now += 1
                            video_index = 1
                        else:
                            video_index += 1
        driver.quit()
        return


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    QApplication.processEvents()
    app = QApplication(sys.argv)

    # WindowClass  인스턴스 생성
    myWindow = WindowClass()

    txt_name_1 = myWindow.txt_name_1
    txt_name_2 = myWindow.txt_name_2
    txt_name_3 = myWindow.txt_name_3
    txt_name_4 = myWindow.txt_name_4

    txt_start = myWindow.txt_start
    txt_end = myWindow.txt_end

    txt_id = myWindow.txt_id
    txt_pw = myWindow.txt_pw

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
