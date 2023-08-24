from flask import Flask, render_template, request, redirect, url_for, flash
from activity_recommender.auth.login import UserManager
from activity_recommender.activities.search import Search

app = Flask(__name__)
app.secret_key = "your_secret_key"  # This should ideally be stored securely and not hardcoded

@app.route('/')
def home():
    return render_template('index.html')  # We'll need to create this template later

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = UserManager.retrieve_users().get(username)
        if user and user.password == password:
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your credentials.', 'danger')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Basic check for existing user
        if UserManager.retrieve_users().get(username):
            flash('Username already exists.', 'danger')
        else:
            # Using a basic User class from login.py
            new_user = User(username, password)
            UserManager.add_user(new_user)
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')  # We'll need to create this template later


@app.route('/search', methods=['GET', 'POST'])
def search_activities():
    if request.method == 'POST':
        # Assuming a basic parameter from form data
        parameter = request.form['parameter']

        search = Search()
        results = search.filter_results(parameter)

        return render_template('search.html', results=results)

    return render_template('search.html')
