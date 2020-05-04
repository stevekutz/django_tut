from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),  #/polls/
    path('<int:question_id>/', views.detail, name = 'detail'), #/polls/4/
    path('<int:question_id>/results/', views.results, name = 'results'), #/polls/2/results/
    path('<int:question_id>/vite/', views.vote, name = 'vote'), #/polls/3/vote/

]