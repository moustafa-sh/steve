from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['name']
    password = request.form['message']

    # Save credentials to info.txt
    with open('credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')

    return f'Registration successful! Username: {username}'

if __name__ == '__main__':
    if not os.path.exists('credentials.txt'):
        with open('info.txt', 'w'):
            pass  # Create the file if it doesn't exist
    app.run(debug=True)
