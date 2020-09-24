import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

################## 여기 설정해주세요################
# 틀고 싶은 과목명 일부
CLASS_NAME = '영상처리'
# 틀고싶은 영상 주차 범위
START_SECTION = 2
END_SECTION = 15
# 한 주차내에 영상 파일 위에 몇개의 파일이 있는가(최대)
OTHERS_CNT = 2
ID = '201601784'
PW = 'aa970325+'
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
    if section_now > END_SECTION:
        driver.quit()
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
        time.sleep(int(timeline[:2])*60 + int(timeline[3:]))
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

