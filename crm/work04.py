#encoding:utf-8

#插入input_csv.py
import time;
import datetime
from crm.work05 import ReadFile
#D:\csv\上下班打卡_日报_20190701-20190717.csv
user=[]
data1=[]
user2=[]
stutas=[]
filePath=str(input("请输入路径"))
readict=ReadFile.read_csv(filePath)
for row in readict:
    data2=data1.append(row[0])
    user.append(row[1])
    user2.append(row[1])
    stutas.append(row[10])

    # print(row[1])
user.remove("姓名")
user2.remove("姓名")
user=set(user)
list=list(user)
print(list)
data1.remove(data1[0])
stutas.remove(stutas[0])
dict2={}
count=0
dict={0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六'}
for i in range(0,len(data1)):
    we= datetime.datetime.fromtimestamp(time.mktime(time.strptime(str(data1[i]), "%Y/%m/%d"))).weekday()
    if list[len(list)-1] == user2[i] :
        count=count+1
        dict2[list[len(list)-1]]=count
print(dict2)


