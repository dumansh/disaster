## How to setup the project

- make virtual env using ```python -m venv venv```

- Install necessary packages ```pip install -r requiremts.txt``` 

- make ```.env``` file
- copy ```.env.example``` to ```.env``` file
- change your database name and password in the .env file
- migrate database ```python manage.py migrate```

- run the app ```python manage.py runserver```