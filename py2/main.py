# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from array import array

import pymongo
# Run command of next line on terminel manually to make sure that pymongo connect to Altus successfully
# pip install dnspython
from pprint import pprint
from random import randint
import os


def say_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    pprint(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #pprint("当前系统版本：" + os.getenv("os"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    say_hi('hello world')

    # client = pymongo.MongoClient("mongodb+srv://ziyuan:EzEqhOvlQi1e0CEQ@jpdb.nstve.mongodb.net/sroredb?retryWrites"
    #                              "=true&w=majority")
    # db = client.admin
    # serverStatusResult = db.command("serverStatus")
    # pprint(serverStatusResult)

    country = {
        'province': 'province',
        'city': 'city',
        'district': {'district1', 'district2', 'district3', 'district4'}
    }
    filelocation =  input("粘贴文件路径")
    civ = open("filelocation", "r")
    count = 0
    省份 = []
    市 = []
    区 = []
    tmp_decode1 = ''
    tmp_decode2 = ''
    tmp_decode3 = ''
    info_array = []
    def 获取省份(line):
        info = {
            'line_detail': line[:len(line) - 1],
            'line_length': len(line),
            'decode': line[:6],
            'name': line[7:len(line) - 1]
        }  # 末尾有一个换行符符
        pprint(info)

    for x in civ.readlines(100):
        if tmp_decode1 != x[:2]:
            tmp_decode1 = x[:2]
            tmp_decode2 = ''
            tmp_decode3 = ''
            print(x[7:len(x) - 1])
            #country['province'] = (x[7:len(x) - 1])
            if tmp_decode2 != x[2:2]:
                tmp_decode2 = x[2:2]
                tmp_decode3 = ''
                print(x[7:len(x) - 1])
                #country['city'] = (x[7:len(x) - 1])
                if tmp_decode3 != x[4:2]:
                    tmp_decode3 = x[4:2]
                    print(x[7:len(x) - 1])
                    #country['district'] += (x[7:len(x) - 1])
        #pprint(country)
    print("一共行数:" + str(count))
