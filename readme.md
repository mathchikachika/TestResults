## Installation

To set up and run the project, follow these steps:

1. Create a virtual environment (recommended) and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install the required Python packages from the requirements.txt file:
   ```bash
   pip install -r requirements.txt
   ```
3. Do not forget to add .env file - these are the environment variables you should have: 
    Contact the owner for the following variables.
   ```bash
   MONGO_DETAILS = value
   DB_NAME = value
   ```
2. Run the server using this following commands:
   ```bash
   python -m main.py
   ```
The server should now be accessible at http://localhost:8000/.