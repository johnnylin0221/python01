#02_second.py

s=input("請輸入小時：")
hour = int(s)
s=input("請輸入分鐘：")
minute = int(s)
s= input("請輸入秒：")
second = int(s)
seconds = hour*3600 + minute *60 +second
print("距離0:0:0,過了",seconds,"秒")
