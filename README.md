Forms 
-A simple Twitter-like application built with Django, allowing users to register with filtered usernames and post tweets with images.

Features
-User Registration: Create new user accounts.

-Username Filtering: Prohibits specific words (shit, fuck, bobo) in usernames during registration.

-Tweet Posting: Users can post short text messages (tweets).

-Image Uploads: Attach images to tweets.

-Basic Feed: Displays recent tweets.

-Responsive Design: Utilizes Tailwind CSS for a mobile-friendly interface.

Prerequisites 
Before you begin, ensure you have the following installed on your system:

Python 3.8+: Download Python

pip: Python's package installer (usually comes with Python).

Git: Download Git

Getting Started 
Follow these steps to get your Django project up and running on your local machine.

1. Clone the Repository 
Open your terminal or command prompt and run the following command to clone the project:

git clone <repository_url> # Replace <repository_url> with the actual URL of your repository
cd Forms

2. Create and Activate a Virtual Environment 
It's highly recommended to use a virtual environment to manage your project's dependencies. This keeps your project isolated from other Python projects.

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

3. Install Dependencies 
With your virtual environment activated, install all the required Python packages using pip:

pip install -r requirements.txt

4. Apply Database Migrations 
Django uses migrations to define and evolve your database schema.

python manage.py makemigrations Accounts Tweets
python manage.py migrate

5. Create a Superuser (Optional but Recommended) 
To access the Django admin panel and manage users/tweets, create a superuser:

python manage.py createsuperuser

Follow the prompts to set a username, email, and password.

6. Run the Development Server 
Start the Django development server:

python manage.py runserver

You can now access the application in your web browser at http://127.0.0.1:8000/.

How to Use 
Registering an Account 
Navigate to http://127.0.0.1:8000/Accounts/register/ or click the "Register" link on the homepage.

Fill in your desired username and password.

Username Filtering: Try to use shit, fuck, or bobo (case-insensitive) in your username. The form validation will prevent you from registering with these words.

Submit the form. If registration is successful, you will be automatically logged in and redirected to the "Post a Tweet" page.

Posting a Tweet with an Image 
Ensure you are logged in. If not, go to http://127.0.0.1:8000/Accounts/login/ and log in with your registered account.

Navigate to http://127.0.0.1:8000/Tweets/post/ or click the "Post Tweet" link.

Enter your tweet content in the text area.

Click "Choose File" to select an image from your computer to attach to your tweet (optional).

Click the "Tweet" button to post your tweet.

Your tweet will appear on the same page under "Recent Tweets" and also on the home page (http://127.00.1:8000/).

Project Structure 
Forms/: The main Django project directory.

Forms/settings.py: Project settings, including INSTALLED_APPS, MEDIA_ROOT, MEDIA_URL.

Forms/urls.py: Main URL routing for the project.

Accounts/: Django app for user authentication and registration.

forms.py: Contains UserRegistrationForm with custom username validation.

views.py: Handles registration logic.

urls.py: URL patterns for the Accounts app.

templates/Accounts/register.html: HTML template for the registration page.

Tweets/: Django app for tweet functionality.

models.py: Defines the Tweet model (content, image, user, timestamp).

forms.py: Contains TweetForm for creating new tweets.

views.py: Handles tweet posting logic.

urls.py: URL patterns for the Tweets app.

templates/Tweets/post_tweet.html: HTML template for posting tweets and displaying a feed.

templates/Tweets/home.html: Simple home page template.

Media/: Directory where uploaded tweet images will be stored (created automatically).

templates/: Contains base HTML templates.

main.html: Base template extending HTML with Tailwind CSS and navigation.

.gitignore: Specifies files and directories to be ignored by Git (e.g., venv, db.sqlite3, Media/).

requirements.txt: Lists all project dependencies.

manage.py: Django's command-line utility.

Deployment Notes 
For production deployment, ensure you change DEBUG = True to DEBUG = False in settings.py.

Configure ALLOWED_HOSTS in settings.py for your production domain.

Set up a proper web server (e.g., Gunicorn, Nginx, Apache) to serve your Django application and static/media files.

Use a more robust database (e.g., PostgreSQL, MySQL) instead of SQLite.

Contributing 
Feel free to fork this repository, open issues, or submit pull requests.

License 📄
This project is licensed under the MIT License - see the LICENSE file for details (not included in this example but good practice for real projects).

Enjoy your Forms experience! 🎉
