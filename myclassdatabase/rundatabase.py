import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="database_capstoneclass")
mycursor= mydb.cursor()
#mycursor.execute("Create TABLE customers( customer_id INT PRIMARY KEY, first_name VARCHAR(20),  last_name VARCHAR(20),phone INT,email VARCHAR(100),street VARCHAR(50),city VARCHAR(20), state VARCHAR(20),zip_code VARCHAR(20))");

#mycursor.execute("Create table store ( store_id INT Primary key, store_name VARCHAR(30), phone INT,email VARCHAR(100),street VARCHAR(50),city VARCHAR(20),state VARCHAR(20),zip_code VARCHAR(20))");

#mycursor.execute("Create TABLE staffs ( staff_id INT Primary Key,first_name VARCHAR(20),last_name VARCHAR(20),phone INT,email VARCHAR(100),active Boolean,store_id INT, manager_id INT,FOREIGN KEY(store_id)REFERENCES store(store_id)ON DELETE CASCADE ON UPDATE CASCADE)");

#mycursor.execute("Create table orders ( order_id INT PRIMARY key, customer_id INT,order_status VARCHAR(50), order_date DATE,required_date DATE, shipped_date DATE, store_id INT,staff_id INT)");
mycursor.execute("create table order_items (order_id INT, item_id INT, product_id INT,quantity INT, list_price INT, discount Decimal,Primary key(order_id, item_id),FOREIGN KEY(order_id)REFERENCES orders(order_id)ON DELETE CASCADE ON UPDATE CASCADE)");

mycursor.execute("Show tables")

for y in mycursor:
    print(y)