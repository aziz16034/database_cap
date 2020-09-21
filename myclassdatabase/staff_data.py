import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="database_capstoneclass")
mycursor= mydb.cursor()
store_id =  input("What is your store id?")

staff_id = input("What is your staff id?")

first_name  = input("What is your first name?")
last_name  = input("What is your last name?")

phone = input("What is your phone number?")
email = input("What is your email id?")


manager_id = input("What is your manager id?")

sqlform = "Insert into staffs(store_id, staff_id, first_name,last_name, phone, email,  manager_id) values(%s, %s, %s,%s,%s,%s, %s)"

staffs = [(store_id, staff_id, first_name,last_name, phone, email,  manager_id)]
mycursor.executemany(sqlform,staffs)
mydb.commit()