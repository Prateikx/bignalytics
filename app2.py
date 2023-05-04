from flask import Flask, request, jsonify, render_template
import mariadb

app = Flask(__name__)

# Load database configuration
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'admin',
    'database': 'airbnb'
}


@app.route('/')
def index():
    conn = mariadb.connect(**config)
    print('Mariadb Database Connected')
    try:
        cur = conn.cursor()
        sql = """CREATE TABLE bigdata (
            ID INT AUTO_INCREMENT,
            name VARCHAR(25),
            Age VARCHAR(25),
            Mobile VARCHAR(10),
            Email VARCHAR(25),
            Password VARCHAR(16),
            City VARCHAR(20),
            Education VARCHAR(25),
            Course VARCHAR(25),
            Refferal VARCHAR(25),
            comments VARCHAR(200),
            Availability VARCHAR(25),
            PRIMARY KEY (ID)
        );"""
        # print('Table Created Successfully')
        cur.execute(sql)
        conn.close()
        return render_template('login.html')
    except mariadb.Error as e:
        print(f"Error creating table: {e}")
        return render_template('login.html')


@app.route('/dashboard', methods=["POST"])
def dashboard():
    conn = mariadb.connect(**config)
    # try:
    #     cur = conn.cursor()
    #     sql = 9

    return "dashboard"


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/new_data', methods=["GET", "POST"])
def new_data():
    conn = mariadb.connect(**config)
    data = {
        "Email": request.form["email"],
        "Password": request.form["password11"]
    }
    vals = tuple(data.values())
    try:
        if request.form["password11"] == request.form["password12"]:
            cur = conn.cursor()
            sql = "INSERT INTO bigdata (Email, password) VALUES (?, ?)"
            cur.execute(sql, vals)
            conn.commit()

            cur.close()
            conn.close()

            return render_template('Thankyou.html')
        else:
            return render_template('Signup.html', pop="Both the password should be same!")
    except mariadb.Error as e:
        return jsonify(error=str(e)), 500


@app.route('/submit', methods=["GET", "POST"])
def Submit():
    if request.method == 'POST':
        data = {
            "name": request.form["name"],
            "Age":  int(request.form["age"]),
            "Mobile": request.form["mobile"],
            "Email": request.form["email"],
            "City": request.form["city"],
            "Education": request.form["Education"],
            "Course": request.form["Course"],
            "Refferal": request.form["Refferal"],
            "Availability": request.form["Availability"]
        }

        try:
            conn = mariadb.connect(**config)
            cur = conn.cursor()
            sql = "INSERT INTO mytable (name, age, mobile, Email, City, Education, Course, Refferal, Availability) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            vals = tuple(data.values())
            cur.execute(sql, vals)
            conn.commit()

            cur.close()
            conn.close()
            return render_template('Thankyou.html')
        except mariadb.Error as e:
            return jsonify(error=str(e)), 500


@app.route('/enquiry')
def enquiry():
    return render_template('enquiry.html')


@app.route('/programs')
def programs():
    return render_template('programs.html')


@app.route('/data')
def data():
    try:
        conn = mariadb.connect(**config)
        cur = conn.cursor()
        sql = "SELECT * FROM mytable;"
        cur.execute(sql)
        data = cur.fetchall()
        # print(data)
        conn.close()
        return render_template('mytable.html', mytable=data)
    except mariadb.Error as e:
        return jsonify(error=str(e)), 500


if '__main__' == __name__:
    app.run(debug=True, port=9991)
