from flask import Flask, request, jsonify, render_template
import mariadb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Signup.html')

@app.route('/signup', methods=["POST"])
def signup():
    data = {
        "Email": request.form["email"],
        "Password": request.form["password1"]
    }
    print(data)
    return "success"

if '__main__' == __name__:
    app.run(debug=True, port=8009)