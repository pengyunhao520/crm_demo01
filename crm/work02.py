#encoding:utf-8
import csv

class ReadFile:
    @classmethod
    def read_csv(cls,path):

        with open(path, 'r',encoding="utf-8") as f:
            resd_row = []
            reader = csv.reader(f)
            #获取真正的数据
            for row in reader:
                resd_row.append(row)
            return resd_row
if __name__ == '__main__':
    #C:\上下班打卡_日报_20190701-20190717.csv
    filePath=str(input("请输入路径"))
    reader=ReadFile.read_csv(filePath)

#2.每个用户打卡多少次
tab=[]
for i in reader:
    tab.append(i)

dict1 = {}
for j in range(0,len(tab)):
    if tab[j][6]!="--":
        if tab[j][1] not in dict1:
            dict1[tab[j][1]]=1
        else:
            dict1[tab[j][1]]+=1
for a,b in dict1.items():
    print (a,"打卡",b,"次")