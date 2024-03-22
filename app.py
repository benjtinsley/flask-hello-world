
from flask import Flask
import psycopg2

app = Flask(__name__)

navigation = '''
    <a href="/">Home</a> |
    <a href="/db_test">Database Test</a> |
    <a href="/db_create">Create Table</a> |
    <a href="/db_insert">Insert Data</a> |
    <a href="/db_select">Select Data</a> |
    <a href="/db_drop">Drop Table</a>
    <hr>
'''

@app.route('/')
def hello_world():
    return navigation + '<h1>Hello World from BD Tinsley in 3308!</h1>'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://demo_flask_db_user:Btfg95mH0oYuk4dKUWJPQjCXuVAMVBfm@dpg-cnuul77109ks73ejf7pg-a.oregon-postgres.render.com/demo_flask_db")
    conn.close()
    return navigation + 'Database Connection Successful'

@app.route('/db_create')
def create_table():
    conn = psycopg2.connect("postgres://demo_flask_db_user:Btfg95mH0oYuk4dKUWJPQjCXuVAMVBfm@dpg-cnuul77109ks73ejf7pg-a.oregon-postgres.render.com/demo_flask_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return navigation + 'Table "Basketball" Created Successfully'

@app.route('/db_insert')
def insert_data():
    conn = psycopg2.connect("postgres://demo_flask_db_user:Btfg95mH0oYuk4dKUWJPQjCXuVAMVBfm@dpg-cnuul77109ks73ejf7pg-a.oregon-postgres.render.com/demo_flask_db")
    cur = conn.cursor()    
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return navigation + 'Table "Basketball" Successfully Polulated'

@app.route('/db_select')
def select_data():
    conn = psycopg2.connect("postgres://demo_flask_db_user:Btfg95mH0oYuk4dKUWJPQjCXuVAMVBfm@dpg-cnuul77109ks73ejf7pg-a.oregon-postgres.render.com/demo_flask_db")
    cur = conn.cursor()
    if cur.rowcount == 0:
        return navigation + 'Error: Table "Basketball" is Empty.'

    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response = '<table>'
    for record in records:
        response += '<tr>'
        for field in record:
            response += '<td>' + str(field) + '</td>'
        response += '</tr>'
    response += '</table>'
    return navigation + response

@app.route('/db_drop')
def drop_table():
    conn = psycopg2.connect("postgres://demo_flask_db_user:Btfg95mH0oYuk4dKUWJPQjCXuVAMVBfm@dpg-cnuul77109ks73ejf7pg-a.oregon-postgres.render.com/demo_flask_db")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return navigation + 'Table "Basketball" Successfully Dropped'