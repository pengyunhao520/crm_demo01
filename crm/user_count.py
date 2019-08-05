#encoding:utf-8

#插入input_csv.py
from crm.input_csv import ReadFile
#C:\Users\Administrator\Desktop\上下班打卡_日报_20190701-20190717.csv
dict=[]
filePath=str(input("请输入路径"))
readdict=ReadFile.read_csv(filePath)
for rea in readdict:
    dict1=dict.append(rea[1])

set=(dict1)
print(set)