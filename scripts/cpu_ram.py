import psutil
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PASSORD123",
    database="exsamen_cpuram"
)

cursor = conn.cursor()

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent

sql = "INSERT INTO system_cpu (cpu, ram) VALUES (%s, %s)"
cursor.execute(sql, (cpu, ram))

conn.commit()
conn.close()

print("Data Lagret!")
print("CPU:", cpu)
print("RAM:", ram)
