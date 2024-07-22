how to run

# Create the virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Verify that the virtual environment is active
(env) your-prompt$

cd backend

#making a migration
python3 manage.py makemigrations

# applying the migration
# provision the database so that it has correct table  and eveything setup

# do this everytime to create new database
python3 manage.py migrate

# run the application
python3 manage.py runserver

#run chrome
http://127.0.0.1:8000/

# to register
http://127.0.0.1:8000/api/user/resgister/

# to get token
http://127.0.0.1:8000/api/token/

#frontend directory which has react install
npm create vite@latest frontend -- --template react

Vanilla
JavaScript

cd frontend

#axios- for network req
npm install axios react react-dom jwt-decode

# frontend
npm run dev
