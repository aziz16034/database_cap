import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345")
mycursor= mydb.cursor()

mycursor.execute("Create database database_capstoneclass ")

#mycursor.execute("Show databases")


for x in mycursor:
    print(x)
