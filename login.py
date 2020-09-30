import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="tinder")

mycursor = conn.cursor()

# Lines to create Database. No longer needed
#mycursor.execute("CREATE DATABASE tinder")
#conn.commit()

# Step 2 Create a Table
# user_id - Int --> Primary Key --> Not Null -- Auto_Increment
# name - Varchar -- Not Null
# email - Varchar -- Not Null
# password - Varchar -- Not Null

mycursor.execute("CREATE TABLE proposals (proposal_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, romeo INT NOT NULL, juliet INT NOT NULL)")
conn.commit()

# Create
#mycursor.execute("INSERT INTO users (user_id, name, email, password) VALUES (NULL, 'Rohit Sharma','rohit@gmail.com','rohit')")
#conn.commit()

# Retrieve
