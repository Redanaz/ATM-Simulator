import mysql.connector as sqltor
import random
#_checklist_functions_
def Exists(acc):
    con=sqltor.connect(host='localhost', user='root', password='mysql@zaid', database='bank')
    if con.is_connected()==False:
        print('Error, connection not established')
    else:
        cur=con.cursor()
        st='SELECT AccountNo FROM Bank_Balance'
        cur.execute(st)
        AccNo=cur.fetchall()
        if (acc,) in AccNo:
            return True
        else:
            return False
    con.close()
def Pin_No(pin,acc):
    con=sqltor.connect(host='localhost', user=' root ', password='mysql@zaid',database='bank')
    if con.is_connected()==False:
        print('Error, connection not established')
    else:
        cur=con.cursor()
        st='SELECT PinNo FROM Bank_Balance WHERE AccountNo=%s'%(acc,)
        cur.execute(st)
        p=cur.fetchone()
        if (pin,)==p:
            return True
        else:
            return False
    con.close()
def exists_phoneno(no):
    con=sqltor.connect(host='localhost', user=' root ', password='mysql@zaid',database='bank')
    if con.is_connected()==False:
        print('Error, connection not established')
    else:
        cur=con.cursor()
        st='SELECT PhoneNO FROM Bank_Acc_Info'
        cur.execute(st)
        data=cur.fetchall()
        if (no,) in data:
            return True
        else:
            return False
    con.close()
def Amm(acc,amount):
    con=sqltor.connect(host='localhost', user=' root ', password='mysql@zaid',database='bank')
    if con.is_connected()==False:
        print('Error, connection not established')
    else:
        cur=con.cursor()
        st='SELECT Balance FROM Bank_Balance WHERE AccountNo=%s'%(acc,)
        cur.execute(st)
        a=cur.fetchone()
        if a[0]>=amount:
            return True
        else:
            return False
    con.close()
#_atmfunctions_
def Transfer(acc,acc2, amount):
    if Exists(acc):
        if Exists(acc2):
            pin=int(input('Enter your 4 digit pin number:'))
            if Pin_No(pin,acc):
                if Amm(acc,amount):
                    con=sqltor.connect(host='localhost', user=' root ', password='mysql@zaid',database='bank')
                    if con.is_connected()==False:
                        print('Error, connection not established')
                    else:
                        cur=con.cursor()
                        st1='UPDATE Bank_Balance SET Balance=Balance-{} WHERE AccountNo={}'.format(amount,acc)
                        cur.execute(st1)
                        con.commit()
                        st2='UPDATE Bank_Balance SET Balance=Balance+{} WHERE AccountNo={}'.format(amount, acc2)
                        cur.execute(st2)
                        con.commit()
                        print('Transfered Successfully')
                        st3='SELECT Balance FROM Bank_Balance WHERE AccountNo=%s'%(acc,)
                        cur.execute(st3)
                        data=cur.fetchone()
                        print('The current balance in your account is:-',data[0])
                        con.close()
                else:
                    print('The amount your trying to transfer exceeds your balance in the account')
            else:
                print('Wrong Pin Number')
        else:
            print('A Account that goes by the number,',acc2,'does not exist. Please enter valid account numbers.')
    else:
        print('A Account that goes by the number,',acc,'does not exist. Please enter valid account numbers.')
def Deposit(acc,amount):
    if Exists(acc):
        pin=int(input('Enter your 4 digit pin number:'))
        if Pin_No(pin,acc):
            con=sqltor.connect(host='localhost', user=' root ', password='mysql@zaid',database='bank')
            if con.is_connected()==False:
                print('Error, connection not established')
            else:
                cur=con.cursor()
                st='UPDATE Bank_Balance SET Balance=Balance+{} WHERE AccountNo={}'.format(amount,acc)
                cur.execute(st)
                con.commit()
                st2='SELECT Balance FROM Bank_Balance WHERE AccountNo=%s'%(acc,)
                cur.execute(st2)
                print('Deposit Successful')
                data2=cur.fetchone()
                print('The current Balance in your account is:-',data2[0])
                con.close()
        else:
            print('Wrong Pin Number:')
    else:
        print('The given Account number does not exist, Please enter a valid account number')
def Create_Acc():
    no=int(input('Enter a 10 digit phone number:'))
    if len(str(no))==10:
        if exists_phoneno(no):
            print('The phone number already exists by another account holder. Please enter another phone number')
        else:
            ssn=int(input('Enter your 8 digit social security number:'))
            if len(str(ssn))==8:
                fn=input('Enter your First Name:')
                ln=input('Enter your last name:')
                DOB=input('Enter your date of birth in the form (YYYY-MM-DD):')
                if int(DOB[0:4])<=2006:
                    print('To Create an account, a minimum deposit of 300 rupees is needed')
                    bal=float(input('Enter the amount of money u want to deposit:'))
                    if bal>=300:
                        con=sqltor.connect(host='localhost', user=' root ', password='mysql@zaid',database='bank')
                        if con.is_connected()==False:
                            print('Error, connection not established')
                        else:
                            cur=con.cursor()
                            st1='SELECT PinNo FROM Bank_Balance'
                            cur.execute(st1)
                            data1=cur.fetchall()
                            while True:
                                a=random.randint(1000,9999)
                                if a in data1:
                                    continue
                                else:
                                    pin=a
                                    break
                                st2='SELECT AccountNo FROM Bank_Balance'
                                cur.execute(st2)
                                data2=cur.fetchall()
                                while True:
                                    b=random.randint(10000000000,99999999999)
                                    if b in data2:
                                        continue
                                    else:
                                        acc=b
                                        break
                                    st3='INSERT INTO Bank_Acc_Info VALUES({},{},"{}","{}",{},{},"{}")'.format(acc,ssn,fn,ln,no,pin,DOB)
                                    cur.execute(st3)
                                    con.commit()
                                    st4='INSERT INTO Bank_Balance VALUES({},{},{})'.format(acc,bal,pin)
                                    cur.execute(st4)
                                    con.commit()
                                    con.close()
                                    print('Your Account has been Successfully created')
                                    print('Your Account number is:-',acc)
                                    print('Your Pin number is:-',pin)
                    else:
                        print('Please deposit an amount more than 300.')
                else:
                    print('Account cannot be created for citizens below the age of 18')
            else:
                print('Please enter a valid social security number of 8 digits')
    else:
        print('Please enter a valid phone number of 10 digits')
def Witham(acc,amount):
    if Exists(acc):
        pin=int(input('Enter your 4 digit pin number:'))
        if Pin_No(pin,acc):
            if Amm(acc,amount):
                con=sqltor.connect(host='localhost',user=' root',password='mysql@zaid',database='bank')
                if con.is_connected()==False:
                    print('Error, connection not established')
                else:
                    cur=con.cursor()
                    st='UPDATE Bank_Balance SET Balance=Balance-{} WHERE AccountNo={}'.format(amount,acc)
                    cur.execute(st)
                    con.commit()
                    st2='SELECT Balance FROM Bank_Balance WHERE AccountNo=%s'%(acc,)
                    cur.execute(st2)
                    print('Withdrawal Successful')
                    data3=cur.fetchone()
                    print('The current Balance in your account is:-',data3[0])
                    con.close()
            else:
                print('The amount you are trying to withdraw exceeds your balance in the account')
        else:
            print('Wrong Pin Number')
    else:
        print('The given Account Number does not exist. Please enter a valid Account Number.')
def Balance_Enquiry(acc):
    if Exists(acc):
        pin=int(input('Enter your 4 digit pin number:'))
        if Pin_No(pin,acc):
            con=sqltor.connect(host='localhost',user=' root',password='mysql@zaid',database='bank')
            if con.is_connected()==False:
                print('Error, connection not established')
            else:
                cur=con.cursor()
                st='SELECT Balance FROM Bank_Balance WHERE AccountNo=%s'%(acc,)
                cur.execute(st)
                data4=cur.fetchone()
                print('The current Balance in your account is:-',data4[0])
                con.close()
        else:
            print('Wrong Pin Number')
    else:
        print(' The given Account Number does not exist. Please enter a valid Account Number.')
def Close_Acc(acc):
    if Exists(acc):
        pin=int(input('Enter your 4 digit pin number:'))
        if Pin_No(pin,acc):
            con=sqltor.connect(host='localhost',user=' root',password='mysql@zaid',database='bank')
            if con.is_connected()==False:
                print('Error, connection not established')
            else:
                cur=con.cursor()
                st='SELECT Balance FROM Bank_Balance WHERE AccountNo=%s'%(acc,)
                cur.execute(st)
                data=cur.fetchone()
                if data[0]==0:
                    st2='DELETE FROM Bank_Balance WHERE AccountNo=%s'%(acc,)
                    cur.execute(st2)
                    con.commit()
                    st3='DELETE FROM BANK_Acc_Info WHERE AccountNo=%s'%(acc,)
                    cur.execute(st3)
                    con.commit()
                    print('Account closed successfully')
                    con.close()
                else:
                    print('''Unable to close the existing account due to the balance remaining in the account.Please withdraw the balance to successfully close your account.''')
        else:
            print('Wrong Pin Number')
    else:
        print(' The given Account Number does not exist. Please enter a valid Account Number.')
#_main_
while True:
    print('ATM FUNCTIONS')
    print('1.Open a New Account')
    print('2.Close your Account')
    print('3.Withdraw Money')
    print('4.Deposit Money')
    print('5.Transfer Money')
    print('6.Bank Balance')
    print('7.Exit')
    ch=int(input('Enter your option:'))
    if ch==1:
        Create_Acc()
    elif ch==2:
        acc=int(input('Enter your account number:'))
        Close_Acc(acc)
    elif ch==3:
        acc2=int(input('Enter your account number:'))
        amount=int(input('Enter the amount of money you want to witdraw:'))
        Witham(acc2,amount)
    elif ch==4:
        acc=int(input('Enter your account number:'))
        amount=int(input('Enter the amount of money you want to deposit:'))
        Deposit(acc,amount)
    elif ch==5:
        acc=int(input('Enter your account number:'))
        acc2=int(input('Enter the account number to transfer:'))
        amount=int(input('Enter the amount of money you want to transfer:'))
        Transfer(acc,acc2,amount)
    elif ch==6:
        acc=int(input('Enter your account number:'))
        Balance_Enquiry(acc)
    elif ch==7:
        break
    else:
        print('Invalid Option.')
print('Session Expired')