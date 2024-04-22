# -*- coding: utf-8 -*-

#实验效果：代码切换不同的模式。
#接线：使用windows或linux电脑连接一块arduino主控板，哈士奇接到I2C口SCL SDA
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_huskylens import Huskylens

Board("xugu").begin()  #初始化，选择板型和端口号，不输入端口号则进行自动识别

husky = Huskylens()



husky.command_request_algorthim("ALGORITHM_FACE_RECOGNITION")
#husky.command_request_algorthim("ALGORITHM_OBJECT_TRACKING")
#husky.command_request_algorthim("ALGORITHM_OBJECT_RECOGNITION")
#husky.command_request_algorthim("ALGORITHM_LINE_TRACKING")
#husky.command_request_algorthim("ALGORITHM_COLOR_RECOGNITION")
#husky.command_request_algorthim("ALGORITHM_TAG_RECOGNITION")
#husky.command_request_algorthim("ALGORITHM_OBJECT_CLASSIFICATION")

