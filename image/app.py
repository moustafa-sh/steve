import flask
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        with open('credentials.txt', 'a') as f:
            f.write(f"{name}:{message}\n")
        return redirect(url_for('index'))  # Redirect back to index
    else:
        return render_template('message.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        name = request.form['name']
        game_input = request.form['range']
        with open('like.txt', 'a') as f:
            f.write(f"{name}:{game_input}\n")
        return redirect(url_for('index'))  # Redirect back to index
    else:
        return render_template('game.html')

if __name__ == '__main__':
    app.run(port=10000, debug=True)
