#python函数
#函数的定义
"""
def func1(a,b,c):


    return  a+b+c
"""
#函数的调用
#使用return,定义函数时，需要prin(funct1())调用
#print(func1(1, 2, 3))


#默认参数 指的是定义函数funct2里面的a=1


def func2(a=1):
    print(a)
#func2(3)


#关键字参数  指的是调用函数funct3里面的w=4,e=2,q=1
#def func3(q,w,e):
#    print("q=",q)
#    print("w=",w)
#    print("e=",e)

#func3(w=4,e=2,q=1)


#lambda表达式
# fun4 = lambda x,y :x**y
# print(fun4(2,4))