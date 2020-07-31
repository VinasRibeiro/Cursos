***Settings***
Documentation       Código base apara abrir um sessão com o appium server

Library     AppiumLibrary

Resource        kws.robot


***Keywords***
# Hooks
Open Session
    Open Application        http://127.0.0.1:4723/wd/hub
    ...                     automationName=UIAutomator2
    ...                     platformName=Android
    ...                     deviceName=Emulator
    ...                     app=${EXECDIR}/app/ninjachef.apk
    ...                     udid=emulator-5554
    ...                     adbExecTimeout=50000


Close Session
    Capture Page Screenshot
    Close Application