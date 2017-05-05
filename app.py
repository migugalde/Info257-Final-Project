from flask import Flask, render_template, request, redirect
import sqlite3 as lite
import sys
import time
app = Flask(__name__)

@app.route("/")
def goToLogin():
	con = lite.connect("UCBerkeley.db")
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM Counselor")
		print (cur.fetchall())
	

@app.route("/login" , methods=["GET", "POST"])
def loginScreen():
	if request.method == "GET":
		return render_template("login.html", **locals())
	else:
		username = request.form['username']
		password = request.form['password']
		status = request.form['status']
		con = lite.connect("UCBerkeley.db")
		with con:
			cur = con.cursor()
			if status == 'Student':
				'''
				cur.execute("SELECT username, id from Student WHERE Student.username = username, Student.password = password values ('{}', '{}')".format(username, password))
				student = cur.fetchall()
				'''
				student_query = "SELECT username, id from Student WHERE Student.username = '{username}', Student.password = '{password}'".format(username = username, password = password)
				cursor.execute(student_query)
				student = cur.fetchone()
				if (len(student) > 0):
					student_username = student[0]
					student_id = student[1]
					return redirect("/student/" + str(student_id))
				else:
					return redirect("/login")
			else:
				print (username, password, status)
				cur.execute("SELECT username, id From Counselor WHERE username = '{username}' AND password = '{password}'".format(username = username, password = password))
				#" + str(username) + "AND password = " + str(password))
				#+ str(username) + ", Counselor.password = "+ str(password))
				#'{username}', Counselor.password = '{password}'".format(username = username, password = password))
				counselor = cur.fetchone()
				print(counselor)
				if len(counselor) > 0:
					#logged_counselor = cur.fetchone()
					counselor_username = logged_counselor[0]
					counselor_id = logged_counselor[1]

					return redirect("/counselor/" + str(counselor_id) )
				else:
					return redirect("/login")

@app.route("/student/<int:id>")
def studentPage(id):
	return ("Hello World")
	'''
	if request.method == "GET":
		con = lite.connect("UCBerkeley.db")
		with con:
			cur = con.cursor()
			cur.execute("SELECT * FROM Appointment WHERE Appointment.studentID = " + str(id))
			app_rows = cur.fetchall()
			return render_template("student.html", **locals())
	else:
		date = request.form['date']
		time = request.form['time']
		con = lite.connect("UCBerkeley.db")
		with con:
			cur = con.cursor()
			cur.execute("SELECT majorName FROM Student WHERE Student.id = " + str(id))
			studentMajor = cur.fetchall()#[0]?
			cur.execute("SELECT id FROM Counselor WHERE Counselor.majorName = " + str(studentMajor))
			counselorID = cur.fetchall()#[0]?
			cur.execute("insert into Appointment (counselorID, studentID, time , appDate) values ('{}', '{}','{}', '{}')".format(counselorID, id, time, date))
			cur.execute("SELECT * FROM Appointment WHERE Appointment.studentID = " + str(id))
			app_rows = cur.fetchall()
			return render_template("student.html", **locals())
	'''

@app.route("/counselor/<int:id>")
def counselorPage(id):
	print('Hello World')
	'''
	con = lite.connect("UCBerkeley.db")
	with con:
		cur = con.cursor()
		todayDate = time.strftime("%x")
		cur.execute("SELECT appID, studentID, studentName, time WHERE Appointment.counselorID = " + str(id) + "Appointment.studentID = Student.id);")
		todays_app = cur.fetchall()
		return render_template("counselor.html", **locals())
		'''

@app.route("/studentInfo/<int:id>")
def studentInfo(id):
	con = lite.connect("UCBerkeley.db")
	with con:
		cur = con.cursor()
		cur.execute("SELECT majorName, ethcnicity  from Student WHERE Student.id = " + str(studentID) + " ;")
		student= cur.fetchone()
		major = student[0]
		etchnicity = student[1]
		cur.execute("SELECT majorName, gpaReq, collegeName FROM Major, College WHERE Major.majorName = "+ str(major) + ";")
		major_info = cur.fetchall()
		return render_template("studentInfo.html", **locals())

if __name__ == "__main__":
	app.run()