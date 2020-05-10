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
        now = timezone.now()
        day_ago = now - datetime.timedelta(days = 1)
        
        # same as day_ago <= self.pub_date and self.pub_date <= now   
        return day_ago <= self.pub_date <= now    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)    

    def __str__(self):
        return self.choice_text    