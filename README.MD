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
    - entering `deactivate` will leave exit virtual environment 
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
    - Map the app view to a URL using a `URLconf` 
    - Update the project's `root URLconf`
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
 - inside `mysite/urls.py`, add the `path('polls/', include('polls.urls'))`
    ~~~ py
    urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
    ]
    ~~~
4) Restart the server and goto `http://127.0.0.1:8000/polls/`
- You should see the view in the browser
<img src = "polls_view.png"/>

#### Set up Database
1) Create the database (SQLite by default):
    - `python manage.py migrate`
2) Create `Question` and `Choice` models
- Each model is  class that represents the `shape` of you app's data
    ~~~ py
    import datetime

    from django.db import models
    from django.utils import timezone

    # Create your models here.
    class Question(models.Model):
        question_text = models.CharField(max_length = 200)
        pub_date = models.DateTimeField('date published')

        def __str__(self):
            return self.question_text

        def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    

    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete = models.CASCADE)
        choice_text = models.CharField(max_length = 200)
        votes = models.IntegerField(default = 0)    

        def __str__(self):
            return self.choice_text  
    ~~~
3) Update `mysite/settings.py`
- in `polls/apps.py` the configuration class is defined
~~~ py
class PollsConfig(AppConfig):
    name = 'polls'
~~~
- add the following line inside of `settings.py` to reference this configuation class
    ~~~ py
    INSTALLED_APPS = [
        'polls.apps.PollsConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ~~~
4) Use `makemigrations` to let Django know that models were updated
    ~~~ bash
    python manage.py makemigrations polls
    ~~~
5) Migrate changes into database
    ~~~ bash
    python manage.py migrate    
    ~~~
### The overall flow is
- Create models in the app's `models.py`
- Create migrations using `python manage.py makemigrations`
- Run the migrations using `python manage.py migrate`