import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="database_capstoneclass")
mycursor= mydb.cursor()

order_id = input("What is your order id?")
customer_id = input("What is your customer id?")

order_status = input("What is your order status?")
order_date = input("What is your order date?")
required_date = input("What is your required date?")
shipped_date = input("What is your shipped date?")
store_id = input("What is store id?")

staff_id = input("What is your staff id?")

sqlform = "Insert into orders(order_id, customer_id, order_status, order_date, required_date, shipped_date,store_id, staff_id) values(%s, %s, %s,%s,%s,%s, %s, %s)"

orders = [(order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id, staff_id)]
mycursor.executemany(sqlform, orders)
mydb.commit()

store_id = input("What is your store id?")

staff_id = input("What is your staff id?")

first_name = input("What is your first name?")
last_name = input("What is your last name?")

phone = input("What is your phone number?")
email = input("What is your email id?")

manager_id = input("What is your manager id?")

sqlform = "Insert into staffs(store_id, staff_id, first_name,last_name, phone, email,  manager_id) values(%s, %s, %s,%s,%s,%s, %s)"

staffs = [(store_id, staff_id, first_name, last_name, phone, email, manager_id)]
mycursor.executemany(sqlform, staffs)
mydb.commit()


sql = "SELECT \
  store.store_name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)