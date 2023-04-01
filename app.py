
import gpt
import time
from flask import Flask, request,send_file,render_template
from flask_cors import CORS

app = Flask(__name__)
cache_buster = int(time.time())
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/answer', methods=['POST','GET'])
def answer():

    data = request.files['audio']
    gpt.run(data)
    return send_file('./respuesta.wav', mimetype='audio/wav')


if __name__ == '__main__':
    app.run()
    
