# print("hello world!")  # 字符串
# print(123)   #  整数
# print(2.11)  #  小数
# print(True)  #  布尔值
# print(())    #  元组
# print([])    #  数组
# print({})    #  字典 


# a = input("请输入:")
# b = input("请输入:")
# print("两段字符的长度是:",len(a)+len(b))


# 元组，下标（从0开始编号）
# a=(1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)
# print(a[5]) # 打印下标是5的元组
# # 切片
# print(a[:4]) # 左闭右开，不包括下标4
# print(a[4:9])
# print(a[9:]) 

# print(a.index("嘻嘻")) index 查找某个值的下标，就近原则
# print(a.count("哈哈")) count 统计某个值的数量
# 二维元组
# b=(a,"哈哈","嘻嘻")
# print(b[0][3])

# a=[1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False]
# a.append("append")
# print(a)
# # 元组一旦写好过后就不可以修改，而数组是可以修改的
# # a.count() 查找某个值的下标，就近原则
# # a.index() 统计某个值的数量
# # a.append() append 往数组的末尾添加数据
# # a.insert(0,"insert")  insert 往数组中指定的位置插入数据（下标和插入的数据用逗号隔开）
# b = a.pop(5) # 剪切数据,把下标为5的数据剪切出来
# print(b) # 把剪切出来的数据打印出来
# # a.clear() 清空数组
# xx = ["你好","不好"]
# # a.extend(xx) 往数组的末尾添加数据，也可以添加数组
# print (a+xx) # 可以用更简单的方式去实现
# # a.remove("哈哈") 删除某个值
# # True = 1
# # False = 0

"""
python的语法
所有的方法都是小括号结尾。比如，print（），input（），len（）
元组，数组，字典的取值，都是用中括号，比如a[]
元组，数组，字典的定义，分别是(),[],{}

字典的特点
1、字典中的值没有顺序
2、字典的结构必须是键值对的结构：key:value

"""
a = {"name":"张三",0:"哈哈","age":24}
# 取值
print(a["name"])
# 新增
a["high"] = "178cm"
print(a)
# 修改
a["name"] = "李四"
print(a)
b = a.get("name")
print(b)
b = a.pop("name")
print(b)
print(a)
a.update(name="刘武")
print(a)

# 数组和字典的删除
del a["name"]
print(a)

del a[0]

"""

练习：
获取用户输入的个人信息，并且存储到字典中。
个人信息包括了：name,age,sex

"""

name = input("请输入你的姓名：")
age = input("请输入你的年龄：")
sex = input("请输入你的性别：")
# userinfo = {}
# userinfo.update(name=name,age=age,sex=sex)
# print(userinfo)

# userinfo["name"] = name
# userinfo["age"] = age
# userinfo["sex"] = sex

userinfo = {"name":name,"age":age,"sex":sex}
print(userinfo)

元组 
数组/列表 list
字典 