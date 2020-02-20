from app import app

app = Flask(__name__)


@app.route('/')
def index():
    render_template('index.html')

@app.route('/')
def about():
    render_template('about.html')

@app.route('/')
def contact():
    render_template('contact.html')

@app.route('/')
def index():
    render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)