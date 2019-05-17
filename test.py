# -*- coding:utf-8 -*-
import cv2
import numpy as np
cv2.namedWindow("gray")
img = np.zeros((512,512),np.uint8)#生成一张空的灰度图像
cv2.line(img,(0,0),(511,511),255,5)#绘制一条白色直线
cv2.imshow("gray",img)#显示图像
#循环等待，按q键退出
while True:
	key=cv2.waitKey(1)
	if key==ord("q"):
		break
cv2.destoryWindow("gray")
--------------------- 
作者：Joeya_ICT 
来源：CSDN 
原文：https://blog.csdn.net/leaves_joe/article/details/67656340 
版权声明：本文为博主原创文章，转载请附上博文链接！
