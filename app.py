from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/anpr')
def anpr():
    return 'Anpr Details'

if __name__ == "__main__":
    app.run(debug=True, port=8000)