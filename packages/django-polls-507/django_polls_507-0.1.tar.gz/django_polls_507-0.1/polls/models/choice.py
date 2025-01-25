from django.db import models
from polls.models.question import Question

class Choice(models.Model):
  choice_text=models.CharField(max_length=255)
  question=models.ForeignKey(Question, on_delete=models.CASCADE)
  votes=models.IntegerField(default=0)
  
  def __str__(self):
    return self.choice_text
  