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
        sql = """CREATE TABLE mytable (ID INT AUTO_INCREMENT,
                name VARCHAR(25),
                Age VARCHAR(25),
                Mobile VARCHAR(10),
                Email VARCHAR(25),
                City VARCHAR(20),
                Education VARCHAR(25),
                Course VARCHAR(25),
                Refferal VARCHAR(25),
                Availability VARCHAR(25),
                PRIMARY KEY (ID));"""
        print('New Table Created Successfuly')
        cur.execute(sql)
        conn.close()
        return render_template('index.html')
    except:
        print('exception')
        return render_template('index.html')


@app.route('/submit', methods=["POST"])
def Submit():
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
    app.run(debug=True, port=9999)
