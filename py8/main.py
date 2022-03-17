import math
import random

# **********排序10个数
# **********print(random.randint(1,100))1到100的整数
# **********print(random.random())0到1的浮点数
# **********github.com/foreverlz1111


def print_menu():
    print("\n1选择排序\n2冒泡排序\n3插入排序\n4希尔排序\n5递归排序\n6快速排序\n7堆排序\n8计数排序\n9桶排序\n10基数排序\n0退出")

    
def 选择排序():
    length = len(list)
    print("选择排列前：", list)
    i = 0
    while i < length - 1:
        j = i + 1
        while j < length:
            if list[i] > list[j]:  # 注意这里的比较
                tmp = list[i]
                list[i] = list[j]
                list[j] = tmp
            j = j + 1
        i = i + 1
    print("#排列后：", list)


def 冒泡排序():
    length = len(list)
    print("冒泡排列前：", list)
    i = 0
    while i < length:
        j = 0
        while j < length - i - 1:
            if list[j] > list[j + 1]:  # 注意这里的比较
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp
            j = j + 1
        i = i + 1
    print("#排列后：", list)


def 插入排序():
    print("插入排列前：", list)
    i = 0
    for i in range(len(list)):
        j = i - 1
        tmp = list[i]
        while j >= 0 and list[j] > tmp:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = tmp
    print("#排列后：", list)


def 希尔排序():
    print("希尔排列前：", list)
    pos = 1
    while pos < len(list) / 3:
        pos = pos * 3 + 1
    while pos > 0:
        for i in range(pos, len(list)):
            tmp = list[i]
            j = i - pos
            while j >= 0 and list[j] > tmp:
                list[j + pos] = list[j]
                j -= pos
            list[j + pos] = tmp
        pos = math.floor(pos / 3)
    print("#排列后：", list)


def 递归排序(list):
    if len(list) < 2:
        return list
    mid = math.floor(len(list) / 2)
    left, right = list[0:mid], list[mid:]
    return 递归排序操作(递归排序(left), 递归排序(right))


def 递归排序操作(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def 快速排序(list, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(list) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partition_index = 快速排序分块(list, left, right)
        快速排序(list, left, partition_index - 1)
        快速排序(list, partition_index + 1, right)
    return list


def 快速排序分块(list, left, right):
    pivot = left
    index = pivot + 1
    temp = index
    while temp <= right:
        if list[temp] < list[pivot]:
            快速排序交换(list, temp, index)
            index += 1
        temp += 1
    快速排序交换(list, pivot, index - 1)
    return index - 1


def 快速排序交换(list, i, j):
    list[i], list[j] = list[j], list[i]


def 堆排序(list):
    global list_length
    list_length = len(list)
    堆排序最大堆(list)
    print(list)
    for i in range(len(list) - 1, 0, -1):
        堆排序交换(list, 0, i)
        list_length -= 1
        堆排序堆处理(list, 0)
    return list


def 堆排序最大堆(list):
    for i in range(math.floor(len(list) / 2), -1, -1):
        堆排序堆处理(list, i)


def 堆排序堆处理(list, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < list_length and list[left] > list[largest]:
        largest = left
    if right < list_length and list[right] > list[largest]:
        largest = right
    if largest != i:
        堆排序交换(list, i, largest)
        堆排序堆处理(list, largest)


def 堆排序交换(list, i, j):
    list[i], list[j] = list[j], list[i]


def 计数排序(list):
    max_value = max(list)
    bucket_len = max_value + 1
    bucket = [0] * bucket_len
    sorted_index = 0
    length = len(list)
    for i in range(length):
        if not bucket[list[i]]:
            bucket[list[i]] = 0
        bucket[list[i]] += 1
    for j in range(bucket_len):
        while bucket[j] > 0:
            list[sorted_index] = j
            sorted_index += 1
            bucket[j] -= 1
    return list

def 桶排序(list):
    return ("待补充")

def 基数排序(list):
    digit = 0
    max_digit = 1
    max_value = max(list)
    while 10**max_digit < max_value:
        max_digit = max_digit + 1
    while digit < max_digit:
        temp = [[]for i in range(10)]
        for i in list:
            t = int((i/10**digit)%10)
            temp[t].append(i)
        coll = []
        for bucket in temp:
            for i in bucket:
                coll.append(i)
        list = coll
        digit += 1
    return list
    
if __name__ == "__main__":
    list = []
    user_exit = True
    count = 15
    while count > 0:
        rand_temp = random.randint(1, 100)
        list.append(rand_temp)
        count -= 1
    print_menu()
    while user_exit:
        select = input("输入：（0～10数字）")
        match int(select):
            case 0:
                user_exit = False
            case 1:
                选择排序()
            case 2:
                冒泡排序()
            case 3:
                插入排序()
            case 4:
                希尔排序()
            case 5:
                print("排序前：",list)
                print("递归排序后：",递归排序(list))
            case 6:
                print("排序前：",list)
                print("快速排序后：",快速排序(list))
            case 7:
                print("排序前：",list)
                print("堆排序后：",堆排序(list))
            case 8:
                print("排序前：",list)
                print("计数排序后：",计数排序(list))
            case 9:
                print("排序前：",list)
                print("桶排序后：",桶排序(list))
            case 10:
                print("排序前：",list)
                print("基数排序后：",基数排序(list))
            case _:
                print("输入错误！")
                
    # print("#排列后：",递归排序(list))
