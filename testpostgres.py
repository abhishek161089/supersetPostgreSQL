### Test for creating PostgreSQL TABLE and insert queries from the CSV files
import psycopg2
import csv
import time, os, re

BASE_FOLDER = '/media/user-ubuntu/FEE6C709E6C6C0DF/Abhi_data/MCAScrap/master_data_21Apr2018'

try:
	"""
	connect_str = "dbname='testpython' user='user-ubuntu' host='localhost' " +\
			"password='wasd1234'"
	conn = psycopg2.connect(connect_str)
	"""
	conn = psycopg2.connect(database='testpython', user='user-ubuntu', 
							password='wasd1234', host='127.0.0.1', port='5432')
	""
	cursor = conn.cursor()

	#cursor.execute("""CREATE TABLE tutorials (name char(40));""")
	#cursor.execute("""SELECT * from tutorials""")

	#### Create Table for the company
	"""
	cursor.execute('''CREATE TABLE company_master
				(ID SERIAL PRIMARY KEY NOT NULL,
				CORPORATE_IDENTIFICATION_NUMBER TEXT NOT NULL,
				COMPANY_NAME TEXT NOT NULL,
				COMPANY_STATUS TEXT NOT NUll,
				COMPANY_CLASS TEXT,
				COMPANY_CATEGORY TEXT,
				SUB_CATEGORY TEXT,
				DATE_OF_REGISTRATION DATE NOT NULL,
				REGISTERED_STATE TEXT NOT NULL,
				AUTHORIZED_CAPITAL INT NOT NULL,
				PAIDUP_CAPITAL INT NOT NULL,
				INDUSTRIAL_CLASS TEXT,
				PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN TEXT,
				REGISTERED_OFFICE_ADDRESS TEXT NOT NULL,
				REGISTRAR_OF_COMPANIES TEXT NOT NULL,
				EMAIL_ADDR TEXT,
				LATEST_YEAR_ANNUAL_RETURN DATE,
				LATEST_YEAR_FINANCIAL_STATEMENT DATE)
				''')
	"""
	### INSERT Query
	#cursor.execute("INSERT INTO company_master VALUES (%s)")
	#conn.commit()

	cursor.execute("SET datestyle='ISO, DMY';")

	#### Reading from the CSV
	with open(os.path.join(BASE_FOLDER, 'mca_andaman_21042018.csv')) as f:
		reader = csv.reader(f)
		next(reader)

		for row in reader:
			row[6] = row[6].replace("-", "/")
			row[15] = row[15].replace("-", "/")
			row[16] = row[16].replace("-", "/")
			print (row[6], row[15], row[16])
			if 'NA' in row[15:]:
				cursor.execute("INSERT INTO company_master VALUES (DEFAULT, \
							%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
						 row[:15])
			else:
				cursor.execute("INSERT INTO company_master VALUES (DEFAULT, \
							%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
						 row)
			
			#break

	#rows = cursor.fetchall()
	#print (rows)

	conn.commit()
	cursor.close()
	conn.close()
except Exception as e:
	print ("Didn't connect.")
	print (e)
	conn.close()
