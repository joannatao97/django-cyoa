from django.core.urlresolvers import reverse
from django.db import models
from sortedm2m.fields import SortedManyToManyField

# Create your models here.
# used django tutorials

# Question class: Question text, page title, choices shown, input field if needed
class Question(models.Model):
    question_text = models.TextField(max_length=64000)
    title = models.CharField(max_length=200)
    choices = SortedManyToManyField('Choice', blank=True)
    input_field = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title


# Choice class: leads to a question, has text/label
class Choice(models.Model):
    to_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.choice_text


# Adventure class: leads to first question, has a title and description
class Adventure(models.Model):
    first_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title