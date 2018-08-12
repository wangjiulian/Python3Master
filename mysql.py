import pymysql

db = pymysql.connect('localhost','root','','python_master')
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')
# data = cursor.fetchone()
# print('database version: %s' % data)

# sql = """ CREATE TABLE EMPLOYEE(
# id int(11) NOT NULL AUTO_INCREMENT,
# FIRST_NAME CHAR(20) NOT NULL,
# LAST_NAME CHAR(02),
# AGE INT,
# SEX CHAR(1),
# PRIMARY KEY (id),
# INCOME FLOAT )"""


# sql = " INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX) VALUES('小明','王',12,1) "
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME,\
#  LAST_NAME, AGE, SEX, INCOME) \
#  VALUES ('%s', '%s', '%d', '%c', '%d' )" \
#  % ('Mac', 'Mohan', 20, 'M', 2000)


# sql = " SELECT * FROM EMPLOYEE \
# 	  WHERE INCOME > 100 "

# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)

try:
	cursor.execute(sql)
	db.commit()

	# cursor.execute(sql)
	# result = cursor.fetchall()
	# for row in result:
	# 	fname = row[1]
	# 	lastname = row[2]

	# 	print("fname:%s , lastname:%s" % (fname,lastname))

except Exception as e:
	print(e)
	# db.rollback()
finally:
	db.close()








