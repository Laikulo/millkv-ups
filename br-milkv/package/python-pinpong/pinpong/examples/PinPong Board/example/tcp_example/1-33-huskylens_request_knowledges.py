# -*- coding: utf-8 -*-

#实验效果：加载或保存模型
#接线：使用windows或linux电脑连接一块arduino主控板，哈士奇接到I2C口SCL SDA
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_huskylens import Huskylens

ip = "192.168.0.90"
port = 8081

Board(ip, port)

husky = Huskylens()


#husky.command_request_knock()
#       Header	Header 2	Address	  Data Length	Command	 Checksum
#return 0x55	0xAA	    0x11	      0x00	    0x2E	 0x3E

file_index = 1
#保存模型 
# 如果是物体追踪模式下保存的模型，名称为： ObjectTracking_Backup_1.bin
# husky.command_request_save_model_to_SD_card(file_index)
# time.sleep(2)
#加载模型
husky.command_request_load_model_from_SD_card(file_index)
time.sleep(2)









