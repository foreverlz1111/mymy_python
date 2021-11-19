import random
import math
#**********排序10个数
#**********print(random.randint(1,100))1到100的整数
#**********print(random.random())0到1的浮点数

def menu():
    print('1选择排序\n2冒泡排序\n')

def 选择排序():
    print("排列前：",list)
    i = 0
    while(i < 10-1):
        j=i+1
        while(j < 10):
            if list[i] < list[j]:#注意这里的比较
                tmp = list[i]
                list[i] = list[j]
                list[j] = tmp
            j = j+1
        i = i+1
    print("#排列后：",list)


def 冒泡排序():
    print("排列前：",list)
    i = 0
    while(i < 10):
        j = 0
        while(j < 10 - i - 1):
            if list[j] > list[j+1]:#注意这里的比较
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
            j = j+1
        i = i+1
    print("#排列后：",list)

def 插入排序():
    print("排列前：",list)
    i = 0
    for i in range(len(list)):
        j = i - 1
        tmp = list[i]
        while j >= 0 and list[j] > tmp:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = tmp
    print("#排列后：",list)
    
def 希尔排序():
    print("排列前：",list)
    pos = 1
    while( pos < len(list)/3 ):
        pos = pos*3+1
    while pos > 0:
        for i in range(pos ,len(list)):
            tmp = list[i]
            j = i-pos
            while j >= 0 and list[j] > tmp:
                list[j+pos] = list[j]
                j -= pos
            list[j+pos] = tmp
        pos = math.floor(pos/3)
    print("#排列后：",list)

def 递归排序(list):
    if(len(list)<2):
        return list
    mid = math.floor(len(list)/2)
    left,right = list[0:mid],list[mid:]
    return 递归排序操作(递归排序(left),递归排序(right))

def 递归排序操作(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0));
    return result
if __name__ == '__main__':
    list = [random.randint(1,100), random.randint(1,100), random.randint(1,100),
            random.randint(1,100), random.randint(1,100), random.randint(1,100),
            random.randint(1,100), random.randint(1,100), random.randint(1,100),
            random.randint(1,100)]

    #print("#排列后：",递归排序(list))
    
