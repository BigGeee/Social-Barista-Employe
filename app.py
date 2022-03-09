from audioop import add
from flask import Flask, render_template, url_for, request, redirect
import pyrebase
from dbInit import config, firebase, auth, db
from collections import OrderedDict

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return redirect(url_for('employeeOrders'))

@app.route('/employeeOrders/')
def employeeOrders():
    userIDS = []
    all_users = db.child("fav_db").get()
    for userID in all_users.each():
        userIDS.append(userID.key())

    empList = []
    orderKeys = []
    for currUser in userIDS:
        usersEmp = db.child("fav_db").child(currUser).get()
        print(currUser)
        for obj in usersEmp.each():
            if obj.key() != "cart":
                empList.append(obj.val())
                orderKeys.append(obj.key())

    return render_template('employeeOrders.html', empList = empList , orderKeys = orderKeys, db =db )

if __name__ == '__main__':
    app.run()
