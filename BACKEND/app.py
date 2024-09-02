from flask import Flask
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'



db.init_app(app)

#web route to check functionality 
@app.route('/')
def index():
    return "code check one two"


if __name__ == '__main__':
    # ensures that any changes are effected in real time
    app.run(debug=True)