# Project Name

This is a brief description of your project.

## Installation

Follow these steps to set up the project environment:

### 1. Clone the Repository

```bash
git clone https://github.com/mugiwara35/jublia_test.git
cd jublia_test
2. Create a Python Virtual Environment
bash
Copy code
python -m venv env
3. Install Requirements
bash
Copy code
pip install -r requirements.txt
4. Install Redis for Windows
Download Redis from this link and extract the files.

5. Start Redis Server
Open a terminal, navigate to the Redis directory, and start the server:

bash
Copy code
redis-server
6. Run Celery Worker
Open another terminal, activate the environment, and start Celery:

bash
Copy code
.\env\Scripts\activate  # Activate the virtual environment on Windows
celery -A celery_worker worker --pool=solo --loglevel=info
7. Run the Flask Application
Open a third terminal, activate the environment, and run the Flask application:

bash
Copy code
.\env\Scripts\activate  # Activate the virtual environment on Windows
python app.py
8. Access the Application
Open your web browser and go to http://localhost:5000 to access the application.

go
Copy code

Terima kasih atas kesabaran Anda! Silakan salin ini ke dalam file `README.md` Anda. 
