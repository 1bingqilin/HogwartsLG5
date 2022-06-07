import os
import sys
import re
import yaml
from test_3 import func2

print(dir())
func2(3)
"""
1.元素分类

有如下值集合[11,22,33,44,55,66,77,88,99,90], 将所有大于66的值保存至字典的第一个key中，将小于66值保存至第二个key的值中。
"""
list1 = [11,22,33,44,55,66,77,88,99,90]
dict2 = {}
value1 =[]
value2 =[]

for i in list1:
    if i > 66:
        value1.append(i)
    elif i < 66:
        value2.append(i)
dict2.update(key1=value1,key2=value2)
print(dict2)

"""
2.输出商品列表，用户输入序号，显示用户选中的商品。

商品   li = ["手机", "电脑", "鼠标垫", "游艇" ]

a. 允许用户添加商品

b. 用户输入序号显示内容

li = ["手机", "电脑", "鼠标垫", "游艇" ]
a = input("添加商品： ")
li.append(a)
print(li)
b = int(input("请输入序号： "))
print(li[b])

"""
"""
5. 有两个列表

l1 = [11, 22, 33]

l2 = [22, 33, 44]

a. 获取内容相同的元素列表
"""
l1 = [11, 22, 33]
l2 = [22, 33, 44]
m =[]
for i in l1:
    for j in l2:
        if i == j:
            m.append(i)
print(m)

"""
b. 获取l1中有， l2中没有的元素列表
"""
"""
l1 = [11, 22, 33]
l2 = [22, 33, 44]
n =[]

for i in l1:
    if i not in l2:
        n.append(i)

print(n)
"""
"""
c. 获取l2 中有，l1中没有的元素列表
"""
"""
l1 = [11, 22, 33]
l2 = [22, 33, 44]
p =[]
for j in l2:
    if j not in l1:
        p.append(j)
print(p)
"""
"""
d. 获取l1 和 l2 中内容都不同的元素
"""
l1 = [11, 22, 33]
l2 = [22, 33, 44]
n =[]

for i in l1:
    if i not in l2:
        n.append(i)
for j in l2:
    if j not in l1:
        n.append(j)
print(n)

"""
6.转换

a. 将字符串 s = "alex"转换为列表
"""
"""
s = "alex"
w = list(s)
print(w)
"""
"""
b. 将字符串s = "alex"转换为元组
"""
"""
s = "alex"
w = tuple(s)
print(w)
"""
"""
c. 将列表li = ["alex", "seven"]转换为元组

li = ["alex", "seven"]
l=tuple(li)
print(l)

"""
"""
d. 将元组 tu = ("Alex", "seven")转换为列表
"""
"""

tu = ("Alex", "seven")
t = list(tu)
print(t)
"""

"""
7.利用 for 循环和range输出

a. for循环从大到小输出1-100
"""
"""
for i in range(100,0,-1):
    print(i,end=" ")
"""
"""
b. for 循环从小到大输出100 -1
"""
"""
for i in range(1,101):
    print(i,end=" ")
"""
"""
c. while 循环从大到小输出1-100
"""
"""
i = 100
while i >= 1:
    print(i,end=" ")
    i -= 1
"""
"""
d.while 循环从小到大输出100-1
"""
"""
i = 1
while i <= 100:
    print(i,end=" ")
    i += 1
"""
"""
8.购物车

功能要求：

要求用户输入总资产，例如：2000

显示商品列表，让用户根据序号选择商品，加入购物车购买，如果商品总额大于总资产，提示余额不足，否则，购买成功。
"""
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
pric = input("请输入总资产： ")
dict = {}
sum = 0
num =1
for i in goods:
    n = i["name"]
    dict.update({num:n})
    num += 1
print(dict)




















