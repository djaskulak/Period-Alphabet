from flask import Flask, render_template
from pymongo import MongoClient
import config
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

load_dotenv()
DB_URI = os.getenv('DB_URI')
app = Flask(__name__)
app.config.from_object('config.Config')
client = MongoClient(DB_URI)
db = client.get_database('generaldb')
letters = db.periodalpha

# @app.route('/')
# def index():
#     """Return homepage."""
#     return render_template('home.html', msg='Welcome to Period Alphabet')


@app.route('/')
def letters_index():
    """ Show all the letters of the Period Alphabet """
    return render_template('letters_index.html', letters=letters.find())


@app.route('/letters/<letter_id>')
def one_letter(letter_id):
    ''' Show one letter '''
    letter = letters.find_one({'_id': ObjectId(letter_id)})
    return render_template('one_letter.html', letter=letter)

if __name__ == '__main__':
    app.run(debug=True)
