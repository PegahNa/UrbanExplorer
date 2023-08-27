from flask import Flask, render_template, request, redirect, url_for, flash, session
from activity_recommender.auth.login import UserManager, User
from activity_recommender.activities.search import Filter
from activity_recommender.utils.flask_utils import get_data_for_city

app = Flask(__name__)
app.secret_key = "app_secret_key"  # This should ideally be stored securely and not hardcoded

# load users into memory from the JSON file
try:
    UserManager.retrieve_users()
except Exception as e:
    print(f"Error loading users: {e}")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template("menu.html")


@app.route('/flask_login', methods=['GET', 'POST'])
def flask_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username, password)
        if user.login():
            flash('Logged in successfully!', 'success')
            session["logged_in"] = True
            return render_template("menu.html")
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
        price = request.form['price']
        rating = request.form['rating']
        wheelchair = 'wheelchair' in request.form
        hearing = 'hearing' in request.form
        visual = 'visual' in request.form

        # Fetch city data
        data_city = get_data_for_city(city)

        # If only city is provided as a filter, return all activities for that city
        if not (price or rating or wheelchair or hearing or visual):
            return render_template('search.html', results=data_city)

        # Apply filters
        search = Filter(data_city=data_city, city=city)
        if price:
            search.filter_by_price(price)
        if rating:
            search.filter_by_rating(rating)
        if wheelchair:
            search.filter_by_wheelchair_accessible_entrance()
        if hearing:
            search.filter_by_hearing_accessibility()
        if visual:
            search.filter_by_visual_accessibility()

        # Fetch the final filtered results after applying all filters
        results = search.filtered_results

        return render_template('search.html', results=results)
    return render_template('search.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)


