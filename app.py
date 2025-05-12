from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['email'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        session['email'] = email
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/deploy', methods=['POST'])
def deploy():
    if 'email' not in session:
        return redirect(url_for('login'))
    code = request.form.get('code')
    file = request.files.get('file')
    # Placeholder logic
    return "Project Deployed at: /aryan/" + session['email']

if __name__ == '__main__':
    app.run(debug=True)
