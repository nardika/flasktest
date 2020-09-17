import MySQLdb
from flask import Flask, redirect, render_template, request

db_host = "localhost"
db_user = "root"
db_password = ""
db_database = "test"
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('./index.html', title='Welcome')

@app.route('/users')
def showusers():
    db = MySQLdb.connect(db_host, db_user, db_password, db_database)
    cursor = db.cursor()
    sql = "SELECT id, username FROM users"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render_template('./users.html', title='Welcome', members=results)

@app.route('/profile/<name>')
def profile(name):
    db = MySQLdb.connect(db_host, db_user, db_password, db_database)
    cursor = db.cursor()
    sql = "SELECT id, username, age, city, DOB, gender FROM users WHERE username = '%s'" % name
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render_template('./profile.html', title='Welcome', user=results[0])

@app.route('/users/add',methods =['POST'])
def add_user():
    db = MySQLdb.connect(db_host, db_user, db_password, db_database)
    cursor = db.cursor()
    sql = "INSERT INTO users (username) Values ('%s')" % request.form['username']
    try:
        cursor.execute(sql)

        db.commit()

    except:
        db.rollback()

    db.close()
    return redirect('/users')

@app.route('/users/delete',methods =['POST'])
def delete_user():
    db = MySQLdb.connect(db_host, db_user, db_password, db_database)
    cursor = db.cursor()
    sql = "DELETE FROM users WHERE username ='%s'" % request.form['user']
    try:
        cursor.execute(sql)

        db.commit()

    except:
        db.rollback()

    db.close()
    return redirect('/users')

@app.route('/users/delete/<id>',methods =['GET'])
def delete_user2(id):
    db = MySQLdb.connect(db_host, db_user, db_password, db_database)
    cursor = db.cursor()
    sql = "DELETE FROM users WHERE id = %s" % id
    try:
        cursor.execute(sql)

        db.commit()

    except:
        db.rollback()

    db.close()
    return redirect('/users')

@app.route('/users/update',methods =['POST'])
def update_user():
    db = MySQLdb.connect(db_host, db_user, db_password, db_database)
    cursor = db.cursor()
    sql = "UPDATE users SET username = '%s', age = '%s', city = '%s', dob = '%s', gender = '%s' WHERE username = '%s' " % (request.form['name'], request.form['age'], request.form['city'], request.form['dob'], request.form['gender'], request.form['name'])

    try:
        cursor.execute(sql)

        db.commit()

    except:
        db.rollback()

    db.close()
    return redirect('/users')

# Some cloud python IDE do not allow the following to be run , hence comment out this code if need be.
if __name__ == "__main__":
    app.run(debug=True)
    pass




