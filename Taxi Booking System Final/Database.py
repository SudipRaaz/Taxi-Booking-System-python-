import mysql.connector

con = mysql.connector.connect(host = "localhost",user = 'root',  database = 'taxi_booking_system')
cursor =con.cursor()


