#python控制流语法
import random
#分支结构  多重分支  嵌套分支（扁平化，不推荐嵌套分支特多，可读性差）
"""
        3x - 5 (x > 1)
f(x) =   x + 2 (-1 <= x < 1)
        5x + 3 (x < -1)
"""

x = int(input("请输入x值： "))
if x >= 1:
    y = 3*x-5
elif -1 <= x < 1:
    y = x+2
else:
    y = 5*x+3
print(y)

#for循环
"""
1、1-100求和
2、加入分支结构实现1-100的偶数求和
3、Python实现1-100的偶数求和
"""
#1-100求和
sum = 0
for i in range(101):
    sum += i
print(sum)

#2、加入分支结构实现1-100的偶数求和
sum_a = 0
for i in range(101):
    if i%2 == 0:
        sum_a += i
print(sum_a)

#3、Python实现1-100的偶数求和
sum_b = 0
for i in range(2,101,2):
        sum_b += i
print(sum_b)

#while循环
#break退出所有循环,continue退出当前循环
"""
猜数字游戏
计算机出一个1-100之间的随机数由人猜
计算机根据人猜出的数字分别
给出提示大一点，小一点，猜对了
"""
computer_number = random.randint(1,100)
while True:
    person_number = int(input("猜数字： "))
    if person_number < computer_number:
        print("大一点")
    elif person_number > computer_number:
        print("小一点")
    else:
        print("猜对了")
        break

