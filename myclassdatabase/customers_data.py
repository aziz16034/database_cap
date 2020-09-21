import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="database_capstoneclass")
mycursor= mydb.cursor()

first_name  = input("What is your first name?")
last_name  = input("What is your last name?")

customer_id = input("What is your customer id?")
phone = input("What is your phone number?")
email = input("What is your email id?")
street = input("What is your street?")
city = input("What is your city?")


state = input("What is your state?")
zip_code = input("What is your zip_code?")

sqlform = "Insert into customers(first_name, last_name, customer_id, phone, email, street,city, state, zip_code) values(%s, %s, %s,%s,%s,%s, %s, %s,%s)"

customers = [( first_name, last_name, customer_id, phone, email, street, city, state, zip_code)]
mycursor.executemany(sqlform,customers)
mydb.commit()