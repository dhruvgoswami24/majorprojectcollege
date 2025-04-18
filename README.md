# 📈 Stock Price Predictor

A machine learning-based web app to predict stock prices using historical data. Built with Python and Flask, featuring a clean UI with Bootstrap.

## 🗂 Project Structure

. ├── app.py # Main Flask application ├── utils.py # Utility functions for data processing and prediction ├── model.pkl # Pre-trained ML model for stock prediction ├── requirements.txt # List of Python dependencies ├── requirement # (Optional: possibly a duplicate or unused) ├── Procfile # For deployment on Heroku ├── static/ # Static assets like CSS, JS │ └── style.css ├── templates/ # HTML templates (Jinja2) │ └── index.html ├── stock price predictor/ # (Optional: may contain extra files, confirm its purpose) └── pycache/ # Python cache files

markdown
Copy
Edit

## 🚀 Features

- Predict future stock prices from historical data
- Clean and responsive UI using Bootstrap
- Interactive visualizations
- Flask-powered backend
- Ready for deployment (Heroku supported)

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dhruvgoswami24/majorprojectcollege.git
   cd majorprojectcollege
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python app.py
Open in browser:

cpp
Copy
Edit
http://127.0.0.1:5000/
🌐 Deployment
To deploy on Heroku:

Install Heroku CLI and log in.

Run the following commands:

bash
Copy
Edit
heroku create your-app-name
git add .
git commit -m "Initial commit"
git push heroku master
heroku open
📌 Notes
The utils.py file contains reusable functions like data preprocessing and model loading.

The model.pkl file is a pre-trained ML model used for predictions.

The app uses templates in templates/ and static assets from static/.

👨‍💻 Author
dhruv giri goswami , group number 23

