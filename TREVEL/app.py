from flask import Flask, render_template, request

app = Flask(__name__)

# Definindo a rota principal do site 
@app.route('/')
def home ():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True) 