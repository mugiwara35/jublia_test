# Project Name

This is a brief description of your project.

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
python app.py
```
### 5. Access the Application
Open your web browser and go to http://localhost:5000 to access the application.
