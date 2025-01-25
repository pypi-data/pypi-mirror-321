from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

class Question(models.Model):
    question_text = models.TextField(max_length=400)
    pub_date = models.DateTimeField("date published")


    @admin.display(
        boolean=True, 
        description='Published recently?'  
    )
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text
