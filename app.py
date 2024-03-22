
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from BD Tinsley in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://demo_flask_db_user:Btfg95mH0oYuk4dKUWJPQjCXuVAMVBfm@dpg-cnuul77109ks73ejf7pg-a.oregon-postgres.render.com/demo_flask_db")
    conn.close()
    return 'Database Connection Successful'