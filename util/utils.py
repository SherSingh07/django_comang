
from company.settings import USERNAME, PASSWORD
import psycopg2



def save(sql_query):
	conn = psycopg2.connect(database="oms", user="oms", password="123", host="127.0.0.1")
	print "Opened database successfully"
	cur = conn.cursor()
	cur.execute(sql_query)
		
	print "Table created successfully"
	conn.commit()
	conn.close()



def save_atten_to_database(attendence_data):
	for key in attendence_data:

		#name of the employee
		name = key.split('-')[0]

		# day of the employee		
		day = key.split('-')[1]

		#attendence of the employee
		att = attendence_data[key]

		print 'attendence of : ----' + key.split('-')[0] + '-----for the day : -----' + key.split('-')[1] + ' --- is :---' + attendence_data[key] 

		sql_query = ("update department_attendence set" + " day" + "%d = " + "'%s'" + " where name = " + "'%s'")%(int(day), att, name)
		print(sql_query)
		save(sql_query)
	
	return 'attendence saved'

