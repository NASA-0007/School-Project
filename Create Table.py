import  mysql.connector as sql
# Run this Program Before Running the Main Program (Only Once)
conn=sql.connect(host='localhost',user='root',passwd='glhf123', database='bank')
if  conn.is_connected():
    print('connected succesfully')
cur = conn.cursor()
cur.execute('create database bank')
cur.execute('create table customer_details(acct_no int primary key,acct_name varchar(25),phone_no bigint(25),address varchar(25),cr_amt float)')
cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null)')
