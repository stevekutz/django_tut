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

#### Set up first view
- A view function, or view for short, is a Python function that takes a Web request and returns a Web response
- <a href = "https://docs.djangoproject.com/en/3.0/topics/http/views/" > See Writing Views for more info </a>
- The overall process flow is:
    - Write `view` function inside the app's `views.py`
    - Map the view to a URL using a `URLconf` 
1) Add the following to `polls/views.py`
    ~~~ py
    from django.http import HttpResponse

    # Create your views here.
    def index(request):
        return HttpResponse("Hello, world. This is the poll's index.")
    ~~~
2) Create a `urls.py` in the the polls app and add the following:
    ~~~ py
    from django.urls import path

    from . import views

    urlpatterns = [
        path('', views.index, name = "index"),

    ]
    ~~~

 3) Point the root URLconf in the project to the `polls.url` module 
 - inside `mysite/urls.py`, add the `path('polls/', include('polls.urls')),`
    ~~~ py
    urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
    ]
    ~~~
4) Restart the server and goto `http://127.0.0.1:8000/polls/`
- You should see the view