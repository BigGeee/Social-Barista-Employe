from audioop import add
from flask import Flask, render_template, url_for, request, redirect
import pyrebase
from dbInit import config, firebase, auth, db
from collections import OrderedDict

app = Flask(__name__)



"""
Description: Function to redirect user to employee page on app launch

Params: none
Output: Redirects user to employee page

"""
@app.route('/')
def hello_world():  # put application's code here
    return redirect(url_for('employeeOrders'))



"""
Description: Renders the employee page orders, queueires the database for all user orders and passes
them to the HTML page to be displayed.

Params: none

Output: databse reference, list of orders and order keys. Renders HTML Page
"""
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
