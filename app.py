from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key for session security

# Dummy user data (replace with a database in a real application)
users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'}
]

@app.route('/')
def home():
    return render_template('didno.html')
@app.route('/home1')
def home1():
    return render_template('success1.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken
        if any(user['username'] == username for user in users):
            flash('Username already taken. Choose another one.', 'error')
        else:
            # Store the user data (in-memory storage, replace with a database)
            users.append({'username': username, 'password': password})
            flash('Account created successfully. Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match
        if any(user['username'] == username and user['password'] == password for user in users):
            flash('Login successful!', 'success')
            # You might want to set up a session here for a real application
            return redirect(url_for('home1'))
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
