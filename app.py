from flask import Flask, render_template, request
from tensorflow import keras

app = Flask(__name__)
app.debug = True

model = keras.models.load_model('model.h5')

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict(features)
    return render_template('index.html', output=prediction)

if __name__ == '__main__':
    app.run(use_reloader=True)
