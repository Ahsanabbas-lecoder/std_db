from flask import Flask, render_template, request, redirect
import db_connection  # Import the connection file

app = Flask(__name__)

# Route to display employees
@app.route('/employees')
def employees():
    cursor = db_connection.cursor
    cursor.execute("SELECT * FROM emp")
    employees = cursor.fetchall()
    return render_template('employees.html', employees=employees)

# Route to add a new employee
@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        emp_no = request.form['emp_no']
        age = request.form['age']

        cursor = db_connection.cursor
        cursor.execute(
            "INSERT INTO emp (emp_name, emp_email, emp_no, emp_age) VALUES (?, ?, ?, ?)",
            (name, email, emp_no, age)
        )
        db_connection.conn.commit()  # Save changes
        return redirect('/employees')

    return render_template('add_employee.html')

if __name__ == '__main__':
    app.run(debug=True)