#import stuff for the parser
from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt

#import stuff and connect to postgres
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to the database
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Create the Database

try:
  # CREATE DATABASE can't run inside a transaction
  conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
  cur = conn.cursor()
  cur.execute("CREATE DATABASE tcount;")
  cur.close()
  conn.close()
except:
  #print "Could not create tcount"
  continue

#Connecting to tcount

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor. 

cur = conn.cursor()
cur.execute('''CREATE TABLE tweetwordcount
       (words TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()

class TweetCounter(Bolt):
    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]
        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
        # Log the count - just to see the topology running
        #self.log('%s: %d' % (word, self.counts[word]))
		if self.counts[word] == 1:
			cur = conn.cursor()
			#Insert
			cur.execute("INSERT INTO tweetwordcount (words, count) VALUES (word, self.counts[word]);");
			conn.commit()
		elif self.counts[word] > 1:
			cur = conn.cursor()
			#Insert
			cur.execute("UPDATE tweetwordcount SET count=%s WHERE words=%s, (self.counts[word], words);");
			conn.commit()
		else: continue
		conn.close()

