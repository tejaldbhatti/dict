from flask import Flask, render_template , request 
from textblob import TextBlob
from textblob import Word
import nltk
nltk.download('wordnet')
#download model
nltk.download('punkt')
from textblob import Word


nltk.download('averaged_perceptron_tagger')
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('form.html')


@app.route('/submit', methods = ['POST'])
def form_data():
   user_data = request.form.get('user_data')
   #blob = TextBlob(user_data)
   output = Word(user_data).definitions

   return render_template('predict.html', data = f'{output}')

if __name__ == '__main__':   
        app.run(app.run(host='0.0.0.0', port=8080))   