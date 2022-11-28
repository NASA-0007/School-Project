import  mysql.connector as sql

def menu():
    conn=sql.connect(host='localhost',user='root',passwd='glhf123',database='bank')
    cur = conn.cursor()
    conn.autocommit = True
    print('1.CREATE BANK ACCOUNT')
    print('2.TRANSACTION')
    print('3.CUSTOMER DETAILS')
    print('4.DELETE DETAILS')
    print('5.QUIT')
    n=int(input('Enter your CHOICE='))
    if n == 1:
        acc_no=int(input('Enter your ACCOUNT NUMBER='))
        acc_name=input('Enter your ACCOUNT NAME=')
        ph_no=int(input('Enter your PHONE NUMBER='))
        add=(input('Enter your PLACE='))
        cr_amt=int(input('Enter your CREDIT AMOUNT='))
        V_SQLInsert="INSERT INTO customer_details values(" +  str (acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " +add + " ',"+ str (cr_amt) + " );"
        cur.execute(V_SQLInsert)
        print('Account Created Succesfully!!!!!')
        conn.commit()
    if n == 2:
        acct_no=int(input('Enter Your Account Number='))
        cur.execute('select * from customer_details where acct_no='+str (acct_no) )
        data=cur.fetchall()
        count=cur.rowcount
        conn.commit()
        if count == 0:
            print('Account Number Invalid Sorry Try Again Later')
        else:
            print('1.WITHDRAW AMOUNT')
            print('2.ADD AMOUNT')
            x=int(input('Enter your Choice: '))
            if x == 1:
                amt=int(input('Enter withdrawl amount='))
                cur.execute('update customer_details set cr_amt=cr_amt-'+str(amt) +  ' where acct_no=' +str(acct_no) )
                conn.commit()
                print('Account Updated Succesfully!!!!!')
            if x== 2:
                amt=int(input('Enter amount to be added='))
                cur.execute('update customer_details set cr_amt=cr_amt+'+str(amt) +  ' where acct_no=' +str(acct_no) )
                conn.commit()
                print('Account Updated Succesfully!!!!!')
    if n == 3:
        acc=input('Enter your ACCOUNT NO.=')
        acct_no=int(acc)
        cur.execute('select * from customer_details where acct_no='+str(acct_no) )
        if cur.fetchone() is  None:
            print('Invalid Account number')
        else:
            cur.execute('select * from customer_details where acct_no='+str(acct_no) )
            data=cur.fetchall()
            for row in data:
                print('ACCOUNT NO:',acc)
                print('ACCOUNT NAME:',row[1])
                print('PHONE NUMBER:',row[2])
                print('ADDRESS:',row[3])
                print('AVAILABLE BALANCE:',row[4]) 
    if n == 4:
        print('DELETE YOUR ACCOUNT')
        acct_no=int(input('Enter your account number='))
        xx='delete from customer_details where acct_no='+str(acct_no);
        cur.execute(xx)
        print('ACCOUNT DELETED SUCCESFULLY')
    if n == 5:
        quit()

def main():
    conn=sql.connect(host='localhost',user='root',passwd='glhf123',database='bank')
    cur = conn.cursor()
    print('1.REGISTER')
    print('2.LOGIN')
    while True:
        n=int(input('Enter your Choice='))
        if n== 1:
            name=input('Enter a Username=')
            passwd=int(input('Enter a 4 DIGIT Password='))
            V_SQLInsert="INSERT INTO user_table (passwrd,username) values (" +  str (passwd) + ",' " + name + " ');"
            cur.execute(V_SQLInsert)
            conn.commit()
            print('USER created succesfully')  
        elif  n==2 :
                name=input('Enter your Username=')
                passwd=int(input('Enter your 4 DIGIT Password='))
                V_Sql_Sel="select * from user_table where passwrd='"+str (passwd)+"' and username=  ' " +name+ " ' ;"
                cur.execute(V_Sql_Sel)
                if cur.fetchone() is  None:
                    print('Invalid Username or Password')
                else:
                    print()
                    while True:
                        menu()
        else:
            print("Enter a Valid Input")

main()
