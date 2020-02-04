from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('c_and_r_pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return(render_template('index.html', all_pets = pets))

@app.route('/addpet', methods=["POST"])
def addpet():
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());"
    data = {
        'name': request.form['name'],
        'type': request.form['type'],
    }
    test = connectToMySQL('c_and_r_pets')
    test.query_db(query, data)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)