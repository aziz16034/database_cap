import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="database_capstoneclass")
mycursor= mydb.cursor()

order_id  = input("What is your order id?")
customer_id  = input("What is your customer id?")

order_status = input("What is your order status?")
order_date = input("What is your order date?")
required_date = input("What is your required date?")
shipped_date = input("What is your shipped date?")
store_id = input("What is store id?")


staff_id = input("What is your staff id?")

sqlform = "Insert into orders(order_id, customer_id, order_status, order_date, required_date, shipped_date,store_id, staff_id) values(%s, %s, %s,%s,%s,%s, %s, %s)"

orders = [(order_id, customer_id, order_status, order_date, required_date, shipped_date,store_id, staff_id)]
mycursor.executemany(sqlform,orders)
mydb.commit()