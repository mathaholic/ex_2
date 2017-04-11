#readme.sh

#To run this app, create an AWS AMI with Linux, Postgres, Apache Storm, and at least python 2.7
#Use community AMI id ami-bc5a5dab if you are uncertain how to proceed on your own.
#step 1: start your instance based upon the AMI refernced above.  It should be medium
#step 2: log in and start a storm instance
sparse quickstart extweetwordcount
cd extweetwordcount

#step 3: git clone this repo
git clone https://github.com/mathaholic/ex_2

#step 4: verify you have the proper Python dependencies
pip install re
pip install tweepy
pip install

#step 5 mount an EBS volume
mount /dev/xvdf /data

#step 6: start postgres
cd /data
./start_postgres.sh 

#step 7: build the databases required.  This current version of psycopg2 does not really like to do thi
#so you might have to do it manually
cd 
cd extweetwordcount
python db_creation.py

#step 8: start the Storm application
sparse run

#step 9: don't forget to turn it off after a while with CTRL+C!




