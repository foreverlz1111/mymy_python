import pymysql
import datetime
if __name__ == '__main__':
    city = open("book.txt", "r", encoding='gbk')
    db = pymysql.connect(host="",user="",password="",database="")
    cursor = db.cursor()
    print(datetime.datetime.now())
    
    count = len(city.readlines())
    city.seek(0)
    while count > 0:
        str = city.readline()
        mytime = datetime.datetime.now()
        sql = """insert into dict_entity(status,dict_name,dict_value)values(%s,%s,%s)"""
        try:
            cursor.execute(sql,(1,1,1))
            result = cursor.fetchall()
            for row in result:
                print(row)
            db.commit()
            print(count,"插入:",str[:6],str[7:])
        except:
            print("查询失败")
        count = count - 1
    db.close()
    
