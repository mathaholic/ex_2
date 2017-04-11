


#Sample code snippets for working with psycopg


#Connecting to a database
#Note: If the database does not exist, then this command will create the database


import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Create the Database

try:
    cur = conn.cursor()
    cur.execute("CREATE DATABASE tcount;")
    cur.close()
    conn.commit()
    conn.close()
except:
    print("Could not create tcount")

#Connecting to tcount

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")


#Create a Table
#The first step is to create a cursor.
try:
  cur = conn.cursor()
  cur.execute('''CREATE TABLE tweetwordcount1
         (word TEXT PRIMARY KEY     NOT NULL,
         count INT     NOT NULL);''')
  conn.commit()
  conn.close()
except: 
  print('table already exists.')
  


#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query,
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows.

cur = conn.cursor()


#Insert
cur.execute("INSERT INTO tweetwordcount1 (word,count) VALUES ('better_test', 1);")
conn.commit()

#Update
#Assuming you are passing the tuple (uWord, uCount) as an argument
cur.execute("UPDATE tweetwordcount1 SET count=%s WHERE word=%s;", ('better_test', 5))
conn.commit()

#Select
cur.execute("SELECT word, count from tweetwordcount1;")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
conn.commit()

conn.close()
