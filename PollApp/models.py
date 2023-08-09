from django.db import models
from django.utils import timezone
# Create your models here.

# This is the Choice model for the poll that contains the choices for each poll
# The class's str method returns the choice
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# This is the Poll model that contains the question, description and choices from the Choices model 
# The class's str method returns the question
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    description = models.TextField(max_length=200, default="")
    choices = models.ManyToManyField(
        Choice, related_name='related_polls', blank=True)

    def __str__(self):
        return self.question_text

#  This is the Vote model
# When you vote you are opting for a Choice object
# We can select multiple Choices, but there is no restriction if two polls can't have the same option.
# The vote object will refer to Poll and Choice object both
class Vote(models.Model):
    poll = models.ForeignKey(
        Question, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True)
    choice = models.ForeignKey(
        Choice, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.poll.question_text} - {self.choice.choice_text}"