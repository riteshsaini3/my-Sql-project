import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1235",
    database="laxmistore"
)

cursor = db.cursor()

# Sample SQL Query
cursor.execute("""SELECT * FROM sales""")

result = cursor.fetchall()

for row in result:
    print(row)

db.close()
