#encoding:utf-8

#插入input_csv.py
from crm.work05 import ReadFile
#C:\Users\Administrator\Desktop\上下班打卡_日报_20190701-20190717.csv
a=[]
filePath=str(input("请输入路径"))
readict=ReadFile.read_csv(filePath)
for row in readict:
    a.append(row[1])
    # print(row[1])
a.remove("姓名")
b=set(a)
print(len(b))