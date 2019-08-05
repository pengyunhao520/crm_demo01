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
            #返回一个数组
            return resd_row
