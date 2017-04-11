#Connecting to a database
#Note: If the database does not exist, then this command will create the database


import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Create the Database

try:
    cur = conn.cursor()
    cur.execute("CREATE DATABASE tcount")
    cur.close()
    conn.commit()
    conn.close()
except:
    print "Could not create tcount"

#Connecting to tcount

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor.

c
cur.execute('''CREATE TABLE tweetwordcount
       (words TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
#conn.close()


#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query,
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows.

cur = conn.cursor()

#Insert
cur.execute("INSERT INTO tweetwordcount (word,count) \
      VALUES ('test', 1)");
conn.commit()


=================================