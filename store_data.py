import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="database_capstoneclass")
mycursor= mydb.cursor()

store_id  = input("What is your store id?")
store_name  = input("What is your store  name?")

phone = input("What is your phone number?")
email = input("What is your email id?")
street = input("What is your street?")
city = input("What is your city?")


state = input("What is your state?")
zip_code = input("What is your zip_code?")

sqlform = "Insert into store(store_id, store_name, phone, email, street,city, state, zip_code) values(%s, %s, %s,%s,%s,%s, %s, %s)"

store = [(store_id,store_name,  phone, email, street, city, state, zip_code)]
mycursor.executemany(sqlform,store)
mydb.commit()