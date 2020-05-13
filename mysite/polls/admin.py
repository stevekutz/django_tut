from django.contrib import admin

# Register your models here.
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Questin Text Field',  {'fields': ['question_text']}),
        ('Date information', {'fields':['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)    












