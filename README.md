# Email Scheduler Web Application
## Project Description
This project is a simple web application built using Flask that serves as an email scheduler. The main function of the application is to provide a POST endpoint that allows users to store email details in a database for a specific group of recipients. Users can input the following parameters: `event_id`, `email_recipient`, `email_subject`, `email_content`, and a `timestamp` indicating when the email should be sent.

The application features a robust scheduling mechanism that automatically sends the emails at the designated times. Users can also update or cancel scheduled emails if needed.

### Key Features:
- Store email details and recipient information in a database.
- Schedule emails for future delivery based on a specified timestamp.
- Option to cancel scheduled emails **(This is an additional feature to enhance the functionality of the application)**.
- Built-in error handling and validation for user inputs.
- Add a unit test to verify that Celery sends an email correctly.
This project aims to streamline the process of sending scheduled emails, making it easier for users to manage their communications effectively.

## Installation

Follow these steps to set up the project environment:

### 1. Clone the Repository and install requirements

```bash
git clone https://github.com/mugiwara35/jublia_test.git
python -m venv env
env\Scripts\activate
cd jublia_test
pip install -r requirements.txt
```

### 2. Install Redis for Windows
For Windows, download redis from this "https://github.com/MicrosoftArchive/redis/releases" and extract the files.

### 3. Start Redis Server
Open new terminal, navigate to the Redis directory, and start the server (don't close this terminal)
```bash
redis-server
```
### 3. Run Celery Worker
Open another terminal, activate the environment, and start Celery (don't close this terminal)
```bash
.\env\Scripts\activate  # Activate the virtual environment on Windows
celery -A celery_worker worker --pool=solo --loglevel=info
```

### 4. Run the Flask Application
Open a third terminal, activate the environment, and run the Flask application (don't close this terminal):
```bash
.\env\Scripts\activate  # Activate the virtual environment on Windows
cd jublia_test
python app.py
```
### 5. Access the Application
Open your web browser and go to http://localhost:5000 to access the application.

## Notes
### 1. Simple Test 
I am not using a .env file in this project to simplify testing and configuration. To perform testing using unit tests, simply run the following command (assuming you have completed the installation steps):
```bash
.\env\Scripts\activate  # Activate the virtual environment on Windows
cd jublia_test
python test.py
```

### 2. Changing Email Configuration
To change the email configuration, open the `config.py` file in this project. Update the following variables with your email settings: 
```python
MAIL_USERNAME = 'your_email'
MAIL_DEFAULT_SENDER = 'your_email'
MAIL_PASSWORD = 'your_email_password'
```
