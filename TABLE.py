import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='glhf123', database='bank')
if conn.is_connected():
    print('connected succesfully')
cur = conn.cursor()
cur.execute('drop table user_table;')
cur.execute('create table customer_det(acct_no int primary key,acct_name varchar(25),phone_no bigint(25),address varchar(25),cr_amt float);')
