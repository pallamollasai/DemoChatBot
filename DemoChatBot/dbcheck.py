import pymysql

db=pymysql.connect("localhost","root","root","Test")
cursor=db.cursor()

sql="select * from chatbotusers"
try:
	cursor.execute(sql)
	results=cursor.fetchall()

	for row in results:
		if(row[0]=="Bond"):
			print(row[0]),
except:
	print("unable to fetchdata")
db.close()