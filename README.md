# auto_Player

## Outline
It works on the LMS.

I am attending Incheon National University(INU), 

LMS site is http://cyber.inu.ac.kr/

Therefore, you can use this program if you use the same based LMS.

This program used python, pyqt5, and selenium.

* Must be installed chrome ver.95.0.4638.69 (the latest version in 2021.11.10)

## Introduce Version

Before ver.07 : Have to install selenium
After ver.07 : portable

Ver.01 : Dispose due to security issues

Ver.05 : Include chrome_driver

Ver.07 : Include selenium

Ver.08 : Solve close one popup problem

Ver.09 : Available Multiple Inputs & UI improvement for Ubuntu

Ver.10 : Available Multiple Inputs & UI/security improvement  for Windows

---
# Install

## install package
```shel
conda create -n auto_palyer python=3.8
conda activate auto_palyer

pip install mediapipe==0.8.2
pip install selenium
pip install PyQt5
pip install time
pip install os
pip install sys
```

## Download Chrome driver
Chrome Driver : https://chromedriver.chromium.org/downloads
* Choice your version and Window/Linux/mac

## *If you want to make .exe file (recommend to use in ver.10.3 instead those command)
* pyinstaller --onefile --add-binary "chromedriver.exe";"." autoPlayer10.py --hidden-import=selenium
* pyinstaller --uac-admin --add-binary "chromedriver.exe";"." autoPlayer_test.py --hidden-import=selenium
* pyinstaller --uac-admin --windowed --add-binary "chromedriver.exe";"." autoPlayer_test.py --hidden-import=selenium

