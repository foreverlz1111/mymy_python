import os

num18 = eval("abs(-3)+3+6*2")
dir0 = "/tmp"

dic_name ={
    "permissionerror_count":"{} 个无权访问文件夹",
    "empty_count":"{} 个空文件夹",
}
def printpath(path):
    with os.scandir(path) as i:
        for entry in i:
            if entry.is_dir():
                printpath(entry.path)
            if not entry.is_dir():
                print(entry.path[2:])

                
def emptypath(path):
    count = 0
    permission_e = 0
    for root, dirs, files in os.walk(path,topdown=False):
        for name in dirs:
            try:
                if not os.listdir(os.path.join(root,name)):
                # print("null")
                    count += 1
                    print(os.path.join(root,name))
            except PermissionError:
                permission_e += 1
                continue
        # for name in files:
        #     print(os.path.join(root, name))
    print(dic_name["permissionerror_count"].format(permission_e))
    print(dic_name["empty_count"].format(count))


if __name__ == "__main__":
    # os.chdir()
    # printpath(path = None)
    # emptypath(dir0)                       
    
    
