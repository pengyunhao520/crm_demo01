#encoding:utf-8
import csv


class ReadFile:
    @classmethod
    def read_csv(cls,path):

        with open(path, 'r',encoding="utf-8") as f:
            resd_row = []
            reader = csv.reader(f)
            print(reader)
            for row in reader:
                resd_row.append(row)
            return resd_row
if __name__ == '__main__':
    # D:\上下班打卡_日报_20190701-20190717.csv
    list1=[]
    filePath = input("请输入路径")
    reader = ReadFile.read_csv(filePath)
    for row in reader:
        list1.append(row)
        print(list1)

    #第三题：
    daka={}
    for i in range(1, len(list1)):
        if list1[i][1] not in daka:
           daka[list1[i][1]]=list1[i][0]

    for person,num in daka.items():
        endtime=int(list1[-1][0][8:])
        starttime=int(num[8:])
        num=((endtime-starttime+1)-(endtime-starttime+1)//7)*2
        print(person,"\t",num,"\t")