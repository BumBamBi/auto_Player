# auto_Player
 
It works on the LMS.

I am attending Incheon National University(INU), 

LMS site is http://cyber.inu.ac.kr/

Therefore, you can use this program if you use the same based LMS.

This program used python, pyqt5, and selenium.


* Must be installed chrome ver.85.0.4183.121 (the latest version in 2020.09.25)
* File is in "dist" folder(exe)


Before ver.07 : Have to install selenium
After ver.07 : portable

Ver.01 : Dispose due to security issues

Ver.05 : Include chrome_driver

Ver.07 : Include selenium

Ver.08 : Solve close one popup problem

Ver.09 : Available Multiple Inputs & UI improvement for Ubuntu

Ver.10 : Available Multiple Inputs & UI/security improvement  for Windows

---

* Download for Chrome driver
Chrome Driver : https://chromedriver.chromium.org/downloads

* If you want to make .exe file
pyinstaller --onefile --add-binary "chromedriver.exe";"." autoPlayer10.py --hidden-import=selenium
pyinstaller --uac-admin --add-binary "chromedriver.exe";"." autoPlayer_test.py --hidden-import=selenium
pyinstaller --uac-admin --windowed --add-binary "chromedriver.exe";"." autoPlayer_test.py --hidden-import=selenium

