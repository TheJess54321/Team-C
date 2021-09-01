from flask import Flask, request, render_template
import os

app = Flask(__name__)

port = int(os.environ.get('PORT', 33507))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/home1/')
def home1():
    return render_template('home1.html')

@app.route('/home2/')
def home2():
    return render_template('home2.html')

@app.route('/home3/')
def home3():
    return render_template('home3.html')

@app.route('/home4/')
def home4():
    return render_template('home4.html')


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
