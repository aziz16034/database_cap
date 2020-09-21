import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="database_capstoneclass")
mycursor= mydb.cursor()

print("Welcome to your database")

chooseinput = input("Please choose the following: 1) Customers  2)orders 3)staff  4)order Items  5)store:")

for x in chooseinput:
    if int (x) == 1:

        first_name = input("What is your first name?")
        last_name = input("What is your last name?")

        customer_id = input("What is your customer id?")
        phone = input("What is your phone number?")
        email = input("What is your email id?")
        street = input("What is your street?")
        city = input("What is your city?")

        state = input("What is your state?")
        zip_code = input("What is your zip_code?")

        sqlform = "Insert into customers(first_name, last_name, customer_id, phone, email, street,city, state, zip_code) values(%s, %s, %s,%s,%s,%s, %s, %s,%s)"

        customers = [(first_name, last_name, customer_id, phone, email, street, city, state, zip_code)]
        mycursor.executemany(sqlform, customers)
        mydb.commit()
        break

    elif int(x) ==2:

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


    elif int(x) ==3:
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


    elif int(x)==4:
        order_id = input("What is your order_id?")
        item_id = input("What is your item_id?")

        product_id = input("What is your product id?")
        quantity = input("What is your quantity?")
        list_price = input("What is your listed price?")
        discount = input("What is  discount?")

        sqlform = "Insert into order_items( order_id, item_id, product_id, quantity, list_price, discount) values(%s, %s, %s,%s,%s,%s)"

        order_items = [(order_id, item_id, product_id, quantity, list_price, discount)]
        mycursor.executemany(sqlform, order_items)
        mydb.commit()

    elif int(x) ==5:

        store_id = input("What is your store id?")
        store_name = input("What is your store  name?")

        phone = input("What is your phone number?")
        email = input("What is your email id?")
        street = input("What is your street?")
        city = input("What is your city?")

        state = input("What is your state?")
        zip_code = input("What is your zip_code?")

        sqlform = "Insert into store(store_id, store_name, phone, email, street,city, state, zip_code) values(%s, %s, %s,%s,%s,%s, %s, %s)"

        store = [(store_id, store_name, phone, email, street, city, state, zip_code)]
        mycursor.executemany(sqlform, store)
        mydb.commit()



# data = ["yes",'y','Y']
# print("Thank you for inputting data")
# fruits = ["yes", "y", "Y"]
# for y in fruits:
#   x = input("choice")
#   if x == y:
#     break
#
#

