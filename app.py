from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='Welcome to Period Alphabet')

# mock array
letters = [
    { 'title': "A", 'description': 'Absorbancy'},
    { 'title': "B", 'description': 'Blood'}
]

@app.route('/letters')
def letters_index():
    """ Show all the letters of the Period Alphabet """
    return render_template('letters_index.html', letters=letters)

if __name__ == '__main__':
    app.run(debug=True)

 # there is a text chat and an audio call option
 
 #hmm I don't see it? would it have to do with updating?