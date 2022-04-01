Paymob Analytics System.

To run project:

1 - Clone project from GitHub 
    
    git clone https://github.com/Mahmoud59/Paymob.git

2 - In project directory beside requirements directory, 
    create a virtual environment by 

    virtualenv venv
    source venv/bin/activate

3 - Install packages in virtual environment by 

    pip install -r requirements/requirements.txt

    pip install -r requirements/test-requirements.txt 

4 - Create postgresql `paymob` database.

5 - Migrate apps migrations 

    ./manage.py migrate

6 - For Home Page

    127.0.0.1:8000/analytics/index/

7 - For run unit test, run `pytest` in apps src directory.

8 - You can run `flake8 --statistics` for characters limited in one line.

9 - You can run `isort .` for sort importing packages, function, and classes.
