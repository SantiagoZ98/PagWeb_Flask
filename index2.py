from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/index.html')
def inicio():
    return render_template('index.html')

@app.route('/musica.html')
def musica():
    return render_template('musica.html')

@app.route('/peliculas.html')
def peliculas():
    return render_template('peliculas.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)