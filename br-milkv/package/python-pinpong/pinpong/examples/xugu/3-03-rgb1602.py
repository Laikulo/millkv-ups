# -*- coding: utf-8 -*-

#实验效果：控制I2C RGB彩色LCD1602液晶屏幕
#接线：使用windows或linux电脑连接一块arduino主控板，LCD1602接到I2C口SCL SDA
import sys
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_rgb1602 import RGB1602 #从libs导入rgb1602库

Board("xugu").begin()

lcd = RGB1602()

print("I2C RGB1602 TEST...")

lcd.set_rgb(0,50,0);       #设置RGB值

lcd.print("PinPong")       #显示 "PinPong"

lcd.set_cursor(1,1)        #设置光标位置
lcd.print(1234)            #显示数字

while True:
  time.sleep(1)
  lcd.scroll_left()           #滚动显示
