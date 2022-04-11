import os
import sys
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
############################
# github.com/foreverlz1111 #
############################
__author__ = "foreverlz1111"
__license__ = "GPL3.0"

########
# 常量 #
########

__uname = os.uname()
__current_cwd = os.getcwd()

__denote = "*默认在启动文件夹内新建 out文件夹存放学生成绩、student文件夹存放学生答案\n*默认在启动文件夹内读取anwser.xlsx文件作为答案,读取students.xlsx文件作为花名册"
__borderline = "************************************************************"

########
# 变量 #
########

dic_name = {"students_score_out": "成绩输出目录", "students_anwser": "作答输入目录"}
dir_name = {"students_score_out": "out", "students_anwser": "student"}
files_name = {"anwser": "anwser.xlsx","students":"students.xlsx"}


def menu():
    print(__borderline)
    get_sysinfo()
    print(__denote,"\n")
    get_varinfo()
    print(__borderline)


def get_sysinfo():
    if sys.platform.startswith("linux"):
        print(__uname.sysname, __uname.release, __uname.machine)
        # os.chdir("/home")
    elif sys.platform.startswith("win32"):
        print("Windows")
        # os.chdir("c:\windows")


def get_varinfo():
    print("当前启动目录", __current_cwd)
    create_dir()

def create_dir():
    for x in dir_name:
        try:
            p = __current_cwd + "/" + dir_name[x]
            if not os.path.exists(p):
                try:
                    os.mkdir(p)
                except FileNotFoundError:
                    print("位置异常")
            print(dic_name[x], p)
        except:
            pass

def start():
    print("\n","将学生作答放入student文件夹内，按下[回车键]继续:")
    try :
        tmp = input()
        print(tmp)
    except KeyboardInterrupt:
        print("退出")

if __name__ == "__main__":
    menu()
    start()
   
