#!/usr/bin/python

import pickle


""" 
r只读，r+读写，不创建

w新建只写，w+新建读写，二者都会将文件内容清零

（以w方式打开，不能读出。w+可读写）

w+与r+区别：

r+：可读可写，若文件不存在，报错，若干文件存在，覆盖写原有内容
w+: 可读可写，若文件不存在，创建

a：附加写方式打开，不可读
a+: 附加读写方式打开

U：所有行分割符通过Python的输入方法(例#如 read*() )，返回时都会被替换为换行符\n. 

"""
#Base File I/O
f = open('t.txt', 'r+');
f.write('ADDFAFDAF\nEFEFEFEFE\n#########\n12345t5\n');
f.seek(0);
while True:
	record = f.readline();
	if record == '':
		break;
	print(record);
f.close();


#Pickle工具序列化/反序列化
data1 = {'a':1111,'b':[2,3,4,5,6]}

selfref_list = [1,2,3]
selfref_list.append(selfref_list);

output = open('p.txt','wb');

#Pickle dict using protocol 0.
pickle.dump(data1,output);

#Pickle list using the highest protocol available.
pickle.dump(selfref_list,output,-1);

output.close();

pk1_file = open('p.txt','rb');

data1Recv = pickle.load(pk1_file);

print(data1Recv);

listRecv = pickle.load(pk1_file);

print(listRecv);

pk1_file.close();