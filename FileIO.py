#!/usr/bin/python

import pickle

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