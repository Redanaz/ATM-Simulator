import mysql.connector as sqltor
con = sqltor.connect(host='localhost', user='root', passwd='mysql@zaid')
if con.is_connected()==False:
    print('Error, connection not established')
cur=con.cursor()
#_creating_database
st1='CREATE DATABASE IF NOT EXISTS Bank'
cur.execute(st1)
cur.execute('USE Bank')
#_creating_table1
st2='CREATE TABLE Bank_Acc_Info\
(AccountNo BIGINT(20) PRIMARY KEY,\
SocSecNo INT(10),\
FirstName VARCHAR(20),\
LastName VARCHAR(20),\
PhoneNo BIGINT(12),\
PinNo INT(4),\
DOB DATE)'
cur.execute(st2)
#_creating_table2
st3='CREATE Table Bank_Balance\
(AccountNo BIGINT (20),\
Balance FLOAT(15,4),\
PinNo INT(4),\
FOREIGN KEY(AccountNo) REFERENCES Bank_Acc_Info(AccountNo))'
cur.execute(st3)
con.close()