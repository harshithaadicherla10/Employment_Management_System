from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"

#  Database Connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshu@1001",
        database="company"
    )


@app.route('/')
def Home():
    return render_template("register.html")

# Admin Registration

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        mydb = get_db()
        cursor = mydb.cursor()
        cursor.execute(
            "INSERT INTO users (fname,lname,email,username,password) VALUES (%s, %s,%s,%s,%s)",
            (fname,lname,email,username, password)
        )
        mydb.commit()

        return redirect('/login')

    return render_template('register.html')

# Admin Login

@app.route("/login",methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        mydb = get_db()
        cursor = mydb.cursor()
        cursor.execute("select * from users where username = %s and password = %s",(username,password))
        user = cursor.fetchone()

        if user:
            session['admin'] = username
            return redirect('/dashboard')
        
    return render_template('login.html')

# Forgot password
@app.route("/forgot_password",methods=['GET','POST'])
def Forgotpassword():
    if request.method == 'POST':
        username = request.form['username']
        npassword = request.form['npassword']
        
        mydb = get_db()
        cursor = mydb.cursor()
        cursor.execute("update users set password=%s where username=%s",(npassword,username))
        mydb.commit()
        return redirect('/login')
    return render_template('/forgot_password.html')

# Dashboard

@app.route("/dashboard")
def Dashboard():
    if 'admin' not in session:
        return redirect('/login')
    
    mydb = get_db()
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("select * from employee")
    employees = cursor.fetchall()

    return render_template('dashboard.html', employees=employees)

# Add Employee
@app.route('/add_employee',methods=['GET','POST'])
def Add_employee():
    if 'admin' not in session:
        return redirect('/login')
    
    if request.method == 'POST':
        ename = request.form['ename']
        edept = request.form['edept']
        esalary = request.form['esalary']
        ephone = request.form['ephone']

        mydb = get_db()
        cursor = mydb.cursor()
        cursor.execute("insert into employee (ename,edept,esalary,ephone) values (%s,%s,%s,%s)",(ename,edept,esalary,ephone))
        mydb.commit()
        return redirect('/dashboard')
    return render_template('add_employee.html')

# Edit Employee

@app.route('/edit_employee/<int:eid>',methods=['GET','POST'])
def Edit_employee(eid):
    if 'admin' not in session:
        return redirect('/login')
    
    mydb = get_db()
    cursor = mydb.cursor(dictionary=True)

    if request.method == 'POST':
        ename = request.form['ename']
        edept = request.form['edept']
        esalary = request.form['esalary']
        ephone = request.form['ephone']

        cursor.execute("update employee set ename=%s,edept=%s,esalary=%s,ephone=%s where eid=%s",(ename,edept,esalary,ephone,eid))
        mydb.commit()
        return redirect('/dashboard')
    
    cursor.execute("select * from employee where eid=%s",(eid,))
    emp = cursor.fetchone()
    return render_template("edit_employee.html", emp=emp)

# delete

@app.route('/delete_employee/<int:eid>')
def Delete_employee(eid):
    if 'admin' not in session:
        return redirect('/login')
    
    mydb = get_db()
    cursor = mydb.cursor()
    cursor.execute("delete from employee where eid = %s",(eid,))
    mydb.commit()
    return redirect('/dashboard')

# logout
@app.route('/logout')
def Logout():
    session.pop('admin', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)