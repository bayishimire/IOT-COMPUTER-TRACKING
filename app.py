

from flask import Flask, render_template, request
import pymysql


app = Flask(__name__)
DB_HOST='localhost'
DB_USER='root'   
DB_PASSWORD = ''  # default is empty
DB_NAME = 'flask_db'
def connect_db():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME
    )
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])

def greet():
    name = request.form['name']      # ✅ get 'name' from the form
    email = request.form['email'] 
    password = request.form['password']    # ✅ get 'email' from the form

    conn=connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email,password) VALUES (%s, %s,%s)", (name, email,password))
    conn.commit()
    cursor.close()
    conn.close()
    return f"<h2>Hello, {name}! Your email ({email}) has been saved in database don'worries  data saved .</h2><a href='/'>Back</a>"
if __name__ == '__main__':
    app.run(debug=True)

