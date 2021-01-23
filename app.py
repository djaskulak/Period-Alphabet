from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return 'Welcome to Period Alphabet!'

if __name__ == '__main__':
    app.run(debug=True)