# -*- coding: utf-8 -*-

#实验效果：展示红外遥控功能
#接线：uno支持
import sys
import time
from pinpong.board import Board,IRRecv,Pin

Board("xugu").begin()  #初始化，选择板型和端口号，不输入端口号则进行自动识别

def ir_recv3(data):
  print("------Pin3--------")
  print(data)

ir2 = IRRecv(Pin(2))
ir3 = IRRecv(Pin(3),ir_recv3)

while(1):
  v = ir2.read()
  if v:
    print("------Pin2--------")
    print(v)
  time.sleep(0.1)