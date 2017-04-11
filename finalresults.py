#exercise 2 by Nikki Haas
#finalresults.py

# In this step, your task is to develop two simple scripts that query the database, and return specific results as follows:

# finalresults.py

# When passed a single word as an argument, finalresults.py returns the total number of word occurrences in the stream. For example:

# $ python finalresults.py hello
# Total number of occurrences of of "hello": 10
# Running finalresults.py without an argument returns all the words in the stream, and their total count of occurrences, worted alphabetically, one word per line. For example:

# $ python finalresults.py
# $ (<word1>, 2), (<word2>, 8), (<word3>, 6), (<word4>, 1), ...

import psycopg2
import sys
from operator import itemgetter

#Connecting to tcount

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

#if a word was passed, find it and return its frequency
if len(sys.argv) == 2:
        uWord = str(sys.argv[1].lower())


        #Select
        cur.execute("SELECT words, count from tweetwordcount WHERE words= '%s';" % (uWord))
        records = cur.fetchall()

        if len(records) == 0:
                print "%s is not in the database" % (uWord)
        else:
                for rec in records:
                   print 'total number of occurrences of %s: %s' % (rec[0], rec[1])
                   
        conn.commit()

        conn.close()
else:
        cur.execute("SELECT words, count from tweetwordcount;")
        records = cur.fetchall()
        print sorted(records,key=itemgetter(0))