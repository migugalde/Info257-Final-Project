import sqlite3 as lite
import csv
import sys

# this file must be run once to create the database
con = lite.connect("UCBerkeley.db")

collegeFile = ""

majorFile = ""

counselorFile = "Counselor.csv"

studentFile = ""

with con:
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS College (collegeName VARCHAR(255));")
	cur.execute("CREATE TABLE IF NOT EXISTS Major (majorName VARCHAR(255), gpaReq REAL, collegeName VARCHAR);")
	cur.execute("CREATE TABLE IF NOT EXISTS Counselor (counselorName VARCHAR(255), username VARCHAR, password VARCHAR, majorName VARCHAR(255), roomNum VARCHAR(255));")
	cur.execute("CREATE TABLE IF NOT EXISTS Student (studentName VARCHAR(255), username VARCHAR, password VARCHAR, majorName VARCHAR(255), studentGPA REAL);")
	cur.execute("CREATE TABLE IF NOT EXISTS Appointment(appID INTEGER PRIMARY KEY AUTOINCREMENT, counselorID INT, studentID INT, time VARCHAR(10), appDate VARCHAR(255));")

	# Reading in tables
	'''
	college = open(collegeFile,'r') 
	college_read = csv.reader(college) 
	college_toDB = [(i[0]) for i in college_read]

	major = open(majorFile,'r') 
	major_read = csv.reader(major) 
	major_toDB = [(i[0], i[1], i[2]) for i in major_read]
	'''
	counselor = open(counselorFile,'r')
	counselor_read = csv.reader(counselor)
	counselor_toDB = [(i[0], i[1], i[2], i[3], i[4]) for i in counselor_read]
	'''
	student = open(studentFile,'r') 
	student_read = csv.reader(student) 
	student_toDB = [(i[0], i[1], i[2], i[3], i[4]) for i in student_read]
	'''
# insert into corresponding tables
	'''
	cur.executemany("INSERT INTO College (collegeName) VALUES (?);", college_toDB) 
	cur.executemany("INSERT INTO Major (majorName, gpaReq, college) VALUES (?, ?, ?);", major_toDB ) 
	'''
	cur.executemany("INSERT INTO Counselor (counselorName, username, password, majorName, roomNum) VALUES (?,?,?,?,?);", counselor_toDB)
	#cur.executemany("INSERT INTO Counselor (counselorName, username, password, majorName, roomNum) VALUES ('Meg Griffin', 'Meg_Griffin', 'Meg_Griffin1', 'Computer Science', 'Evans 200')")  
	#cur.executemany("INSERT INTO Student (studentName, majorName, studentGPA) VALUES (?,?,?);", college_toDB) 

# adding ids to the tables
	'''
	cur.execute("ALTER TABLE College ADD id INT PRIMARY KEY AUTO_INCREMENT;")
	cur.execute("ALTER TABLE Major  ADD id INT PRIMARY KEY AUTO_INCREMENT;")
	
	cur.execute("ALTER TABLE Student ADD id INT PRIMARY KEY AUTO_INCREMENT;")
	'''
	cur.execute("ALTER TABLE Counselor ADD id INTEGER PRIMARY KEY AUTO_INCREMENT;")

con.commit()
con.close()

