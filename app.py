from flask import Flask, render_template, request
from tensorflow import keras

app = Flask(__name__)
app.debug = True
# TODO : Add prediction feature
# TODO : Add dashboard
model = keras.models.load_model('model.h5')

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/register')
def register():
    return render_template('auth/register.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(use_reloader=True)
