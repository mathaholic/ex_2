#exercise 2 by Nikki Haas
# histogram.py

# The script gets two integers k1,k2 and returns all the words with a total number 
#of occurrences greater than or equal to k1, and less than or equal to k2. For example:

# $ python histogram.py 3,8
# <word2>: 8
# <word3>: 6
# <word1>: 3

import psycopg2
import sys
from operator import itemgetter

#Connecting to tcount

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

#if a word was passed, find it and return its frequency
if len(sys.argv) != 2:
    print "Not enough values given!"

else:   
    r =list(eval(sys.argv[1])) 
    if r[0] >= r[1]:
        print "Please enter a range from lowest to highest."
    else:
        cur.execute("SELECT words, count FROM tweetwordcount WHERE count BETWEEN %d and %d;" % (r[0], r[1]))
        records = cur.fetchall()
        for rec in records:
            print rec[0], ':', rec[1]

