#python基本数据类型与操作
#数字
#int和float
a = 1
b = 1.0
#打印出a和b的值
print(a)
print(b)

#打印出a和b的数据类型
print(type(a))
print(type(b))

#字符串
#\n是转义符换行，打印出\n   可以
# ①str_a = "abc\\n@##@@##"
# ②str_a = r"abc\n@##@@##"
str_a = r"abc\n@##@@##"
#打印出变量str_a的值
print(str_a)
#打印出变量str_a的类型
print(type(str_a))

#字符串的索引
str_b = "abcedfg"
#abcedfg对应的索引0-6 或者-7到-1
#打印出str_b索引=0的值
#print(str_b[索引])
print(str_b[0])
print(str_b[-7])

#字符串的切片
#打印出str_b索引1-6
#start:stop 意思是start>=索引<stop
print(str_b[1:7])
print(str_b[1:])#标准
#打印出步长2，索引1-6
print(str_b[1:7:2])
print(str_b[1::2])


#列表
list_a = [["a","b","c"],1,2,3,True]
list_b = ["a","b","c",1,2,3,False]
#打印出list_a,list_b的值
print(list_a)
print(list_b)

#打印出list_a,list_b的数据类型
print(type(list_a))
print(type(list_b))

#打印出list_a,list_b的索引
print(list_a[0])
print(list_b[0])

#打印出list_a,list_b的切片
print(list_a[0::2])
print(list_b[0::2])






