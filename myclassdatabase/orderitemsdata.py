import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="database_capstoneclass")
mycursor= mydb.cursor()

order_id  = input("What is your order_id?")
item_id  = input("What is your item_id?")

product_id = input("What is your product id?")
quantity = input("What is your quantity?")
list_price = input("What is your listed price?")
discount = input("What is  discount?")



sqlform = "Insert into order_items( order_id, item_id, product_id, quantity, list_price, discount) values(%s, %s, %s,%s,%s,%s)"

order_items = [(order_id,item_id, product_id, quantity, list_price, discount)]
mycursor.executemany(sqlform,order_items)
mydb.commit()