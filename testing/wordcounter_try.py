from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt

#import stuff and connect to postgres
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import re
# Connect to the database


class TweetCounter(Bolt):
    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        # word = tup.values[0]
        word = re.sub(r'\W+', '', tup.values[0])
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
        cur = conn.cursor()
        cur.execute("SELECT words from tweetwordcount where words = %s;", (word))
        records = cur.fetchall()

        # Log the count - just to see the topology running
        #self.log('%s: %d' % (word, self.counts[word]))#self.log('%s: %d' % (word, self.counts[word]))
        if records == []:
            cur = conn.cursor()
            #Insert
            cur.execute("INSERT INTO tweetwordcount(words, count) VALUES (%s, %s);",  (word, self.counts[word]))
            conn.commit()
        else:
            cur = conn.cursor()
            #Insert
            cur.execute("UPDATE tweetwordcount SET count=%s WHERE words=%s;", (self.counts[word], word))
            conn.commit()
        #else: pass
        conn.close()
        self.log('%s: %d' %(word, self.counts[word]))

        from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt

#import stuff and connect to postgres
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import re
# Connect to the database


class TweetCounter(Bolt):
    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        # word = tup.values[0]
        word = re.sub(r'\W+', '', tup.values[0])
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
        # Log the count - just to see the topology running
        #self.log('%s: %d' % (word, self.counts[word]))
        if self.counts[word] == 1:
            cur = conn.cursor()
            #Insert
            cur.execute("INSERT INTO tweetwordcount(words, count) VALUES (%s, %s);",  (word, self.counts[word]))
            conn.commit()
        elif self.counts[word] > 1:
            cur = conn.cursor()
            #Insert
            cur.execute("UPDATE tweetwordcount SET count=%s WHERE words=%s;", (self.counts[word], word))
            conn.commit()
        else: pass
        conn.close()



==============================================

from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt

#import stuff and connect to postgres
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import re
class TweetCounter(Bolt):
    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        # word = tup.values[0]
        word = re.sub(r'\W+', '', tup.values[0])
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
        cur = conn.cursor()
        cur.execute("SELECT words from tweetwordcount;")
        r = cur.fetchall()

        w = 1

        for term in r:
            if word == term[0]:
                w = 0

        if w == 0:
            cur.execute("UPDATE tweetwordcount SET count=%s WHERE words=%s;", (self.counts[word], word))            
        
        if w == 1:
            cur.execute("INSERT INTO tweetwordcount (words,count) VALUES (%s,%s);",self.counts[word])

        conn.commit()
        conn.close()
        # Log the count - just to see the topology running
        #self.log('%s: %d' % (word, self.counts[word]))#self.log('%s: %d' % (word, self.counts[word]))
        # if records == []:
        #     cur = conn.cursor()
        #     #Insert
        #     cur.execute("INSERT INTO tweetwordcount(words, count) VALUES (%s, %s);",  (word, self.counts[word]))
        #     conn.commit()
        # else:
        #     cur = conn.cursor()
        #     #Insert
        #     cur.execute("UPDATE tweetwordcount SET count=%s WHERE words=%s;", (self.counts[word], word))
        #     conn.commit()
        # #else: pass
        # conn.close()
        self.log('%s: %d' %(word, self.counts[word]))
