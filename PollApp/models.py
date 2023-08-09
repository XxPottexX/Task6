from django.db import models
from django.utils import timezone
# Create your models here.

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    description = models.TextField(max_length=200, default="")
    choices = models.ManyToManyField(
        Choice, related_name='related_polls', blank=True)

    def __str__(self):
        return self.question_text
    
class Vote(models.Model):
    poll = models.ForeignKey(
        Question, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True)
    choice = models.ForeignKey(
        Choice, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.poll.question_text} - {self.choice.choice_text}"