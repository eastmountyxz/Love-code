# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:45:47 2016
@author: yxz15
"""
 
from PIL import Image
import os
 
serarr=['@','#','$','%','&','?','*','o','/','{','[','(','|','!','^','~','-','_',':',';',',','.','`',' ']
count=len(serarr)
 
def toText(image_file):
   image_file=image_file.convert("L")#转灰度
   asd =''#储存字符串
   for h in range(0,  image_file.size[1]):#h
      for w in range(0, image_file.size[0]):#w
         gray =image_file.getpixel((w,h))
         asd=asd+serarr[int(gray/(255/(count-1)))]
      asd=asd+'\r\n'
   return asd
 
def toText2(image_file):
   asd =''#储存字符串
   for h in range(0,  image_file.size[1]):#h
      for w in range(0, image_file.size[0]):#w
         r,g,b =image_file.getpixel((w,h))
         gray =int(r* 0.299+g* 0.587+b* 0.114)
         asd=asd+serarr[int(gray/(255/(count-1)))]
      asd=asd+'\r\n'
   return asd
 
 
image_file = Image.open("nana.jpg") # 打开图片
image_file=image_file.resize((int(image_file.size[0]*0.9), int(image_file.size[1]*0.5)))#调整图片大小
 
print('Info:',image_file.size[0],' ',image_file.size[1],' ',count)

try:
   os.remove('./tmp.txt')
except  WindowsError:
    pass
    
tmp=open('tmp.txt','a')
 
 
tmp.write(toText2(image_file))
 
tmp.close()
