from datetime import datetime, timedelta#时间
from array import array  # 数组导入
from print_module import print_module_function
from colorama import init,Fore
import os

sentance = 'logical logi'
print(sentance.upper())#全大写
print(sentance.lower())#全小写
print(sentance.capitalize())  # 首字母大写
print("一共有" + str(sentance.count('o')) + "个o")#计数
first = 'First'
num_one = 1
num_two = 2
second = 'second'
output = 'hello,{} {}'.format(first, second)
print(output)
output = 'hello,{0} {1}'.format(first, second)
print(output.capitalize())
output = f'hello,{first}  {second}'
print(output.capitalize())
number1 = 1
number2 = 2.0
print(number1)
print(float(number1))
print(number2)
print(int(number2))
current_time = datetime.now()
day_one = timedelta(hours=24)  # 用timedelta规定一天为24小时
week_one = timedelta(weeks=1)  # 规定一周
yesterday = current_time - day_one
print("当前时间:" + str(current_time))
print("24小时前的时间: " + str(yesterday))
print("day  :" + str(current_time.day) + "号")
print("month  :" + str(current_time.month) + "月")
print("year  : " + str(current_time.year) + "年")
print("hour  :" + str(current_time.hour) + "点钟")
birthday = "12/1/1989"
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')  # 日期设置
birthday_date_week_ago = birthday_date - week_one
print("生日:" + str(birthday_date))
print(("生日前一周:" + str(birthday_date_week_ago)))
print()
try:
    print(first)
except ZeroDivisionError as e:
    print("不能除以0")
else:
    print("打印结果1" + first)
finally:
    print("打印结果2" + first)
    print()
if num_one >= 1:
    tax = .07
    print("税款  :" + str(tax))
else:
    tax = 0
    print(tax)
if first.lower() == "first" \
        or first.capitalize() == "First":
    print("first字母拼写正确")
else:
    print("first字母配些错误")
print()
if first in output:
    print("first字母拼写正确")
print()
grade_A = 90
grade_B = 60
grade_C = 58
if grade_A and grade_B and grade_C > 50:
    print(grade_B)
if grade_A > 90 and grade_B > 60:
    print(grade_A)
members = ["oli", "alpha", "ten"]
members.insert(1, "goo")  # 第二个作为goo
print(len(members))
print("首字母排序")
members.sort()
print(members)
print()
numbers = array("d")
numbers.append(1)
numbers.append(2)
print(numbers)
print(numbers[1])
print("#从0开始，取1个字符")
numbers2 = numbers[0:1]
print(number2)
print("字典功能/////first对应second")
members2 ={"first":"second"}
members2["third"] = "forth"
print(members2)
print(members2["first"])
index_count = 0
index_count2 =0
print("正在使用while语句：")
while index_count < len(members):
    print(members[index_count])
    index_count = index_count + 1
each = len(members)
print("正在使用for语句：")
for each in members:
    print(members[index_count2])
    index_count2 = index_count2 + 1
notice = "现在输出时间"#一句话
def print_time(sentance):#function
     print(sentance)
     print(datetime.now())
     print()
print_time(notice)
print_module_function(members)
os_version = os.getenv("os")
print(os_version)
def logger(func):
    def wrapper():
        print("notice1")
        func()
        print("notice2")
    return wrapper
@logger
def sample():
    print("notice")
sample()

exit()