from flask import Flask, render_template, request, redirect, url_for, flash, session
from activity_recommender.auth.login import UserManager, User
from activity_recommender.activities.search import Filter
from activity_recommender.utils.api_utils import get_data_for_city

app = Flask(__name__)
app.secret_key = "your_secret_key"  # This should ideally be stored securely and not hardcoded

# load users into memory from the JSON file
try:
    UserManager.retrieve_users()
except Exception as e:
    print(f"Error loading users: {e}")


@app.route('/')
def home():
    return render_template('index.html')  # We'll need to create this template later


@app.route('/flask_login', methods=['GET', 'POST'])
def flask_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username, password)
        if user.login():
            flash('Logged in successfully!', 'success')
            session["logged_in"] = True
            return redirect(url_for('search_activities'))
        else:
            flash('Login failed. Check your credentials.', 'danger')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Using a basic User class from login.py
        new_user = User(username, password)
        UserManager.add_user(new_user)
        flash('Registration successful!', 'success')
        return redirect(url_for('flask_login'))

    return render_template('register.html')  # We'll need to create this template later


@app.route('/search', methods=['GET', 'POST'])
def search_activities():
    if "logged_in" not in session or not session["logged_in"]:
        return redirect(url_for("flask_login"))
    if request.method == 'POST':
        city = request.form['city']
        price = float(request.form.get('price', 0))
        rating = float(request.form.get('rating', 0))
        wheelchair = 'wheelchair' in request.form
        hearing = 'hearing' in request.form
        visual = 'visual' in request.form

        # Fetch city data
        data_city = get_data_for_city(city)

        # Apply filters
        search = Filter(data_city=data_city, city=city)
        results = search.filter_by_price(price)
        results = search.filter_by_rating(rating)
        if wheelchair:
            results = search.filter_by_wheelchair_accessible_entrance()
        if hearing:
            results = search.filter_by_hearing_accessibility()
        if visual:
            results = search.filter_by_visual_accessibility()

        return render_template('search.html', results=results)
    return render_template('search.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('flask_login'))


if __name__ == '__main__':
    app.run(debug=True)


