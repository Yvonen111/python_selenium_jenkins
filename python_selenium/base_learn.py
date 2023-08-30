import keyword

print(keyword.kwlist)
# 2
print("  hyf")
# 3   注释


a = [1, 2, '6', 'hyf']
print("i" in a)
if "i" in a:
    print("yes")
else:
    print("no")

dict_1 = {"id": 1, 'age': 24}
age = dict_1.get("age")  # dict_1['age']    # 字典类型
if age > 18:
    print('成年人{}'.format(age))  # 格式化输出
else:
    print("未成年人")

# 列表 ->  字典 ->  列表   手动
list1 = ['hyf', 'gj', 'hh', 'jj']
dict_2 = {"name": "hyf", "age": "18", "city": "cq"}
dict_3 = {"name": "gj", "age": "81", "city": "cq"}
list2 = [dict_2, dict_3]
print(list2)

# 自动方式
list3 = ['hyf', 'gj', 'hh', 'jj']
list4 = [18, 81, 22, 33]
list5 = ['cq', 'cd', 'sc', 'yc']
list6 = []  # 空列表  ----  存放字典
for i in range(4):  # 0 1 2 3
    dict_4 = dict(name=list3[i], age=list4[i], city=list5[i])  # dict() 内置函数
    list6.append(dict_4)
    # print(list6)
print(list6)


# 函数
def add_sum(num):
    sum = 0
    for i in range(num):
        sum += i
    print(sum)


def function_len(obj):
    if type(obj) == dict or type(obj) == list or type(obj) == str:
        # if isinstance(obj, str) or isinstance(obj, list) or isinstance(obj, dict):
        leng = len(obj)
        if leng >= 5:
            print("true")
        else:
            print("false")
    else:
        print("输入错误")


add_sum(100)

function_len(list1)
function_len((1, 2, 3, 4, 5, 6))  # 列表
function_len([1, 2, 3, 4, 5, 6])  # 元组
