import os
import sys
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import time
from datetime import datetime
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

__denote = "*启动目录自动新建"+dir_name["students_score_out"]+"文件夹存放学生成绩.xlsx文件、"+ dir_name["students_answer"]+"文件夹存放学生答案.xlsx文件\n*默认在启动文件夹内读取answer.xlsx文件作为答案,读取students.xlsx文件作为花名册\n"
__borderline = "************************************************************"
dic_name = {
    "students_score_out": "成绩输出目录",
    "students_answer": "作答输入目录",
    "keyboard_exit": "\n你选择退出，请重新启动程序",
    "add_student": "\n将文件放入指定目录后(文件夹不会被检测到)，按下[回车键]以继续",
    "answer_notfound": "没找到答案文件，请确保其在启动目录并命名为" + files_name["answer"],
    "students_notfound": "没找到花名册文件，请确保其在启动目录并命名为" + files_name["students"],
    "answer_found":__current_cwd + " 目录已找到文件：" + files_name["answer"],
    "students_found":__current_cwd + " 目录已找到文件：" + files_name["students"],
    "choice_notfound":"没找到对应命令，请重新输入。",
    "processing":"处理中...",
    "score_title":["学号","姓名","班级","成绩","题目总分"],
    "missing_title":["学号","姓名","班级","未提交"],
    "yes":"是",
    "save_error":"处理失败！",
    "save_success":"处理成功，查看文件 ",
    "saved_path": __current_cwd + "/" +dir_name["students_score_out"]+"/"
}
__menu_name = {
    "menu":"\n选择菜单：\n",
    "choice1":"输入1：重新查找文件",
    "choice2":"输入2：修改学生的作答",
    "choice3":"输入3：统计未提交作业的学生名单 ",
    "choice_exit":"输入q：退出本程序",
    
}

def print_menu():
    for x in __menu_name:
        print(__menu_name[x])
    print(__borderline)
    
def catch_choice(c):
    # 版本兼容性，暂不升级为match
    if(c == "1"):
        check_files()
        print_menu()
        return True
    elif(c == "2"):
        output_score()
        print_menu()
        return True
    elif(c == "3"):
        output_missing()
        print_menu()
        return True
    elif(c == "4"):
        return True
    elif(c == "q"):
        return False
    else:
        print(dic_name["choice_notfound"])
        print_menu()
        return True
    
def menu():
    print_menu()
    userexit = True
    while userexit:
        try:
            tmp = input()
            userexit = catch_choice(tmp)
            time.sleep(1)
        except KeyboardInterrupt:
            print(dic_name["keyboard_exit"])
            exit()

def output_missing():
    # only check file if missing
    print(dic_name["processing"])
    students = load_workbook(filename = files_name["students"])
    students_sheet1 = students["工作表1"] # 输出的成绩花名册
    students_table = get_table(students_sheet1)
    wb = Workbook()
    ws = wb.active
    ws.append(dic_name["missing_title"])
    for x in students_table:
        try:
            p = students_answer_filename(x[0])
            if not os.path.exists(p):
                x.append(dic_name["yes"])
                ws.append(x)
        except:
            continue
    try:
        wb.save(dir_name["students_score_out"]+"/"+output_xlsx_name("未提交"))
        print(dic_name["save_success"],dic_name["saved_path"]+output_xlsx_name("未提交"))
    except OSError:
        print(dic_name["save_error"])
    print(__borderline)

def output_score():
    # check file for each
    print(dic_name["processing"])
    answer_sheet1 = load_and_sheet1(files_name["answer"])
    answer_table = get_table(answer_sheet1)
    students = load_workbook(filename = files_name["students"])
    students_sheet1 = students["工作表1"] # 输出的成绩花名册
    students_table = get_table(students_sheet1)
    wb = Workbook()
    ws = wb.active
    score_total = get_total(answer_table)
    ws.append(dic_name["score_title"])
    for x in students_table:
        try:
            single = load_workbook(filename = students_answer_filename(x[0]))
            single_sheet1 = single["Sheet"]
            single_table = get_table(single_sheet1)
        except FileNotFoundError:
            pass
        score = 0
        for a in single_table:
            for b in answer_table:
                if a[0]==b[0]:
                    if a[1] == b[1]:
                        score += b[2]
                else:
                    continue
        x.append(score)
        x.append(score_total)
        ws.append(x)
    try:
        wb.save(dir_name["students_score_out"]+"/"+output_xlsx_name("成绩"))
        print(dic_name["save_success"],dic_name["saved_path"]+output_xlsx_name("成绩"))
    except OSError:
        print(dic_name["save_error"])
    print(__borderline)

    
def students_answer_filename(x):
    return dir_name["students_answer"] +"/"+ str(x) + ".xlsx"

def output_xlsx_name(s):
    mytime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = s+str(mytime)+".xlsx"
    return filename

def get_total(t):
    score = 0
    for c in t:
        score += c[2]
    return score
    
def load_and_sheet1(f):
    wb = load_workbook(filename = f)
    sheet1 = wb["工作表1"]
    return sheet1
    
def get_table(sheet):
    cells = []
    table = []
    p = False
    for x in sheet.iter_rows(min_row = 2):
        cells = []
        for cell in x:
            if cell.value is None:
                break
            cells.append(cell.value)
        if cells != []:
            table.append(cells)
    return table
            
def get_sysinfo():
    if sys.platform.startswith("linux"):
        print(__uname.sysname, __uname.release, __uname.machine)
        # time.sleep(1)
        # os.chdir("/home")
    elif sys.platform.startswith("win32"):
        print("Windows")
        # os.chdir("c:\windows")


def get_varinfo():
    print("当前启动目录", __current_cwd)
    create_dir()


def create_dir():
    dir_error =  "位置异常"
    dir_exist = "已存在，跳过新建"
    dir_mk = "已自动新建文件夹"
    for x in dir_name:
        try:
            p = __current_cwd + "/" + dir_name[x]
            if not os.path.exists(p):
                try:
                    os.mkdir(p)
                    print(dir_mk)
                    continue
                except FileNotFoundError:
                    print(dir_error)
            print(dic_name[x], p,dir_exist)
        except:
            continue


def start():
    print(__borderline)
    get_sysinfo()
    print(__denote)
    get_varinfo()
    print(__borderline)
    print(dic_name["add_student"])
    try:
        tmp = input()
        # print(tmp)
        # time.sleep(1)
    except KeyboardInterrupt:
        print(dic_name["keyboard_exit"])
        exit()


def check_files():
    scan_student()  # 学生文件夹
    scan_answer()  # 答案文件
    scan_student_list()  # 花名册文件
    print(__borderline)

def scan_student():
    files_count = 0
    student_dir = __current_cwd + "/" + dir_name["students_answer"]
    with os.scandir(student_dir) as scan:
        for entry in scan:
            if entry.is_file() and entry.name.endswith(".xlsx"):
                files_count += 1
    scan.close()
    print(student_dir, "目录已找到xlsx文件数量：", files_count)
    

def scan_answer():
    try:
        fp = open(files_name["answer"])
    except FileNotFoundError:
        print(dic_name["answer_notfound"])
    else:
        print(dic_name["answer_found"])
        fp.close()


def scan_student_list():
    try:
        fp = open(files_name["students"])
    except FileNotFoundError:
        print(dic_name["students_notfound"])
    else:
        print(dic_name["students_found"])
        fp.close()


if __name__ == "__main__":
    start()
    check_files()
    menu()
