# Django tutorial
### <a href = "https://docs.djangoproject.com/en/3.0/intro/tutorial01/"> Official Documentation </a>
#### Project Setup 
1) Set up virtual environment
    ~~~ bash
    python3 -m venv tut_env
    ~~~
2) Launch virtual environment from VS Code terminal
    ~~~ bash
    source tut_env/bin/activate
    ~~~
3) Install `Django` 
    ~~~ bash
    pip install django
    ~~~
- the version can be verified by running `python3 -m django --version`
4) Create Project within the virtual environment
    ~~~ bash
    django-admin startproject mysite
    ~~~
- Change to the `mysite` directory and verify project is setup correctly by launching server `python manage.py runserver`
- If you accidentally close the terminal in VS Code and need to quit the server, enter the following in a new terminal
    - `sudo kill $(lsof -t -i:8000)` 
5) Create the polls app within the `mysite` folder
    ~~~ bash
    python manage.py startapp polls
    ~~~