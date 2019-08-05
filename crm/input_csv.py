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
    #D:\csv\上下班打卡_日报_20190701-20190717.csv
    filePath=input("请输入路径")
    reader=ReadFile.read_csv(filePath)
    for row in reader:
        row[1]
        print(row[1])