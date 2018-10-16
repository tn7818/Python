#!/usr/bin/python
#编码设定
# -*- coding: UTF-8 -*-
#coding=utf-8
import sys
import pyodbc

print(sys.getdefaultencoding())
print('Hello 中国 !')

#换行符
print('Go \nGo \nGo UP!')
#加运算
print(3+4)

#乘除运算
print(3*5/1)

#负数运算
print(-6/2)

#除0发生异常
#print(5/0)

#指数运算
print(3**2)

#商
print(7//2)

#余数
print(7%2)

#转义符
print('Let\'s go home !')

#多行注释/自动转义(''')或(""")
print("""Good morning
Mr Wang! """)

#使用斜杠(\)多行显示
print('A \
       B \
	   c')

#字符串拼接
print('Hello'+'A')

#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,
print('Line 1',"Line 2")

#字符串索引
word = 'HelpABC'
print('word: ',word)
print('String Length: ',len(word))
#字符串首个字符
print('Word[0]：',word[0])
#字符串首个字符起始的所有字符值
print('Word[0:]：',word[0:])
#字符串首个字符起始，遍历至第二个字符值
print('Word[:2]：',word[:2])
#字符串第二个字符起始，遍历至第四个字符的值
print('Word[2:4]：',word[2:4])
# 字符串倒数第二个字符
print('Word[-2]：',word[-2])
# 字符串最后两个字符
print('Word[-2:]：',word[-2:])
# 字符串除了最后两个字符之外，其前面的所有字符
print('Word[:-2]：',word[:-2])

#列表索引
squares = [1, 4, 9, 16, 25]
print('squares: ',squares)
print('Sequence Length: ',len(squares))
#列表索引返回指定项
print('squares[0]: ',squares[0])
#切割列表并返回新的列表
print('squares[-3:]: ',squares[-3:])
#拼接列表并返回新的列表
print('squares + [36, 49, 64, 81, 100](New Sequece): ',squares + [36, 49, 64, 81, 100])
#列表索引修改指定项值
squares[3] = 32
print('squares[3] = 32: ',squares)
#列表中添加新值
squares.append(216)
print('squares.append(216): ',squares)
#列表替换一些值
squares[2:5] =['C','D','E']
print("squares[2:5] = ['C','D','E']: ",squares)
#列表移除一些值
squares[2:5] =[]
print("squares[2:5] = []: ",squares)
#列表重置
squares[:] =[]
print("squares[:] = []: ",squares)

#创建空元组
tup1 = ();
print('tup1 = (): ',tup1)
print('Array Length: ',len(tup1))
#创建单成员元组
tup2 = (50,);
print('tup2 = (50，): ',tup2)
# 创建一个新的元组
tup3 = tup1 + tup2;
print ('tup3 = tup1 + tup2: ',tup3)
#删除元组
#del tup3;
#print ('del tup3: ',tup3)
#元组索引
tup2 = (1, 2, 3, 4, 5 );
print('tup2: ',tup2)
#元组索引读取第三个元素
print ('tup2[2]: ',tup2[2])
#读取倒数第二个元素
print ('tup2[-2]: ',tup2[-2])
#从第二个开始后的所有元素
print ('tup2[1:]: ',tup2[1:])
#列表转为元组
list1= ['Google', 'Taobao', 'Baidu']
print ("list1= ['Google', 'Taobao', 'Baidu']: ",list1)
tuple1=tuple(list1)
print ('tuple1=tuple(list1): ',tuple1)

#创建字典
dict = {'num':1234, 'Cbyte':'Toms', 'Objlist':[1,4,8]}
print ('dict :',str(dict))
print ("dict['num']", dict['num']);
print ("dict['Objlist']", dict['Objlist'][0]);
#修改字典值
dict['num'] = 5678
print ("dict['num']", dict['num']);
#新增字典值
dict['AddNum'] = 9000
print ("dict['AddNum']", dict['AddNum']);
#删除字典值
#del dict['AddNum'];
#print ("dict['AddNum']", dict['AddNum']);
#清空字典值
dict.clear()
print ('dict :',str(dict));
#删除字典
del dict
print ('dict :',str(dict));





#输入
iparam = input('Please Input Param: ')
print(iparam)



#以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入
#以双下划线开头的（__foo）代表类的私有成员
#以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数
#Python 可以同一行显示多条语句，方法是用分号 ; 分开
print('A');print('B');print('C');

#所有Python的关键字只包含小写字母
#python最具特色的就是用缩进来写模块
print('Layer 1')
if True:
	print('	SubLayer 1')
elif True:
    print('	SubLayer 2')
else:
	print('	SubLayer 3')
print('Layer 3')




#K-DB连接测试
print('PyODBC',pyodbc.version);
try:
	kdconn = pyodbc.connect('DSN=py4kdb;UID=sys;PWD=kdb');
	cursor = kdconn.cursor() 	
	cursor.execute('select * from user_tables') 
	#获取单条记录
	sigdata = cursor.fetchone();
	print('Single Data : %s' %sigdata[0]);
	#获取所有查询结果记录
	#data = cursor.fetchall() 
	#for x in data: 
	#	print (x[0]) 
	cursor.close() 
	kdconn.close()
except Exception as e:
	print('K-DB连接测试失败！\n',e)


