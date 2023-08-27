# UrbanExplorer
UrbanExplorer is a Python program that assists users in finding and filtering activities in various cities.  
The program allows users to search for activities based on different parameters such as price, rating, accessibility, and opening hours.

## File Structure

Here's a basic overview of the main directories and files in this project:

- `/activity_recommender`: The main source code directory.
    - `/activities`: Code related to activities.
      - `/search`: Code specifically for filtering activities based on different parameters.
    - `/api`: API integration to main code
      - `/api_integration`: Code to show an url for a map of each location
    - `/auth`: Code related to user authentication.
      - `/login`: Code specifically for logging in and registering.
    - `/flask_app`: Code to run program using front-end.
      - `/templates`: HTML templates for every functionality
        - `index`: Main page that user sees. It'll take them to login or register
        - `login`: User needs to enter username and password
        - `menu`: Once logged in, user can choose to search activities or log out
        - `register`: User needs to create username and password
        - `search`: It will filter the activities by specific parameters
      - `flask_app`: Script to run the project
    - `/scripts`: Scripts.
      - `/main`: Code specifically for running the program.
    - `/tests`: Unit tests for our code. 
      - `/test_activities`:  Tests specific to activities
        - `/test_search`: Test Filter class
      - `/test_auth`:  Tests specific to authorization
        - `/test_login`: Test for login and registering process
    - `/utils`: Functions with no dependency
       - `flask_utils`: Utils functions specific to flask
       - `login_utils`: Utils functions specific to login
       - `main_utils`: Utils functions specific to main
       - `search_utils`: Utils functions specific to search
- `/data`: Directory for data files.
    - `/locations`: JSON files for storing locations.
    - `/users`: JSON files for storing usernames and passwords.
- `README.md`: This file!
- `.gitignore`: .idea/ & __pycache__/

## Getting Started

### Prerequisites
Python 3.x  
pip (Python package manager)

### Installation
1. Clone this repository:  
git clone https://github.com/your-username/activity-recommender.git


2. Navigate to the project directory:  
`cd activity-recommender`


3. Install required dependencies:  
`pip install -r requirements.txt`

## Usage

### Main Menu

Run the program by executing the `main.py` file:

You'll be prompted to either log in or register. Choose an option and follow the instructions.

### Choosing Activities

After logging in, you'll be prompted to choose a city you're traveling to (Madrid, Paris, or New York).

### Applying Filters

You can filter activities based on different criteria, such as price, rating, accessibility, and opening hours. Select the filters you want to apply, and the program will display the filtered activities.

### Viewing Activities

Once you've applied filters, you can view the list of filtered activities. Choose an activity to see its details. You can also get a URL for the activity's address or go back to the list of activities.

### Using Flask (work in progress)
1. Run the Flask application:  
`python activity_recommender/flask_app/flask_app.py`  

2. Access the application in your browser at http://localhost:5000.

3. Choose to log in or register to start using the Activity Recommender.

### Contributing
Contributions are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -am 'Add new feature'`.
4. Push to your branch: `git push origin feature-name`.
5. Submit a pull request.