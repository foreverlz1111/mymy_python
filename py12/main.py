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
# 变量 #
########
files_name = {"answer": "answer.xlsx", "students": "students.xlsx"}
dir_name = {"students_score_out": "out", "students_answer": "student"}


########
# 常量 #
########

__uname = os.uname()
__current_cwd = os.getcwd()

__denote = "*默认在启动文件夹内新建out文件夹存放学生成绩excel文件、student文件夹存放学生答案excel文件,仅支持xlsx格式\n*默认在启动文件夹内读取answer.xlsx文件作为答案,读取students.xlsx文件作为花名册\n"
__borderline = "************************************************************"
dic_name = {
    "students_score_out": "成绩输出目录",
    "students_anwser": "作答输入目录",
    "keyboard_exit": "\n你选择退出，请重新启动程序",
    "add_student": "\n将学生作答excel文件放入student文件夹内后(文件夹不会被检测到)，按下[回车键]以继续",
    "answer_notfound": "没找到答案文件，请确保其在启动目录并命名为" + files_name["answer"],
    "students_notfound": "没找到花名册文件，请确保其在启动目录并命名为" + files_name["students"],
}


def menu():
    print(__borderline)
    get_sysinfo()
    print(__denote)
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
    print(dic_name["add_student"])
    try:
        tmp = input()
        # print(tmp)
    except KeyboardInterrupt:
        print(dic_name["keyboard_exit"])


def check_files():
    scan_student()  # 学生文件夹
    scan_answer()  # 答案文件
    scan_student_list()  # 花名册文件


def scan_student():
    files_count = 0
    student_dir = __current_cwd + "/" + dir_name["students_answer"]
    with os.scandir(student_dir) as scan:
        for entry in scan:
            if entry.is_file() and entry.name.endswith(".xlsx"):
                files_count += 1
    scan.close()
    print(student_dir, "已找到excel文件数量：", files_count)


def scan_answer():
    try:
        fp = open(files_name["answer"])
    except FileNotFoundError:
        print(dic_name["answer_notfound"])
    else:
        print("当前目录已找到文件", files_name["answer"])
        fp.close()


def scan_student_list():
    try:
        fp = open(files_name["students"])
    except FileNotFoundError:
        print(dic_name["students_notfound"])
    else:
        print("当前目录已找到文件", files_name["students"])
        fp.close()


if __name__ == "__main__":
    #menu()
    #start()
    #check_files()
