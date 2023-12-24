from flask import Flask, flash, render_template, redirect, url_for, request, send_from_directory, send_file
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



app = Flask(__name__)


app.secret_key = "LEapdf8sdufhbcsjkbh345"
Config = {
  "apiKey": "AIzaSyCso5xhjt2kRArS3gw2Z1XnXLrC4R2AJrE",
  "authDomain": "leapgenie.firebaseapp.com",
  "projectId": "leapgenie",
  "storageBucket": "leapgenie.appspot.com",
   "databaseURL":"https://leapgenie-default-rtdb.firebaseio.com/",
  "messagingSenderId": "761201128701",
  "appId": "1:761201128701:web:5d75fd8d5babaac131ba94",
  "measurementId": "G-SLNP1P20B6"
}
cred = credentials.Certificate("leapgenie-firebase-adminsdk-gqwgt-7feec6016e.json")
firebase = pyrebase.initialize_app(Config)
firebase_admin.initialize_app(cred)
database = firebase.database()
db = firestore.client()
auth = firebase.auth()

@app.route('/')
def login():
    return render_template("form.html")

@app.route('/EmailLogin',methods=['POST','GET'])
def EmailLogin():

    if request.method=='POST':
        email=request.form.get("email")
        password=request.form.get("password")
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template("index.html")
        except Exception as e:
            flash("Check your Email and Password")
            return render_template("form.html")
@app.route('/EmailSign', methods=['POST', 'GET'])
def EmailSign():
    if request.method == 'POST':
        name = request.form.get("Username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")  # Correct variable name

        if email is None:
            flash("Email is required")
            return render_template("form.html")
        if password == confirm_password:
            print("58")
            try:
                auth.create_user_with_email_and_password(email, password)
                users_ref = db.collection('users')  # Create a collection named "users"
                user_data = {
                    "name": name,
                    "email": email,
                    "password": password
                }
                new_user_ref = users_ref.add(user_data)
                return render_template("index.html")  # Redirect to the index page after successful registration
            except:
                flash("Check your email | Email Already Exists")
                return render_template("form.html")
        else:
            flash("Please check your password")
            return render_template("form.html")
    elif request.method == 'GET':
        return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)
