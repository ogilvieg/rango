from django.db import models
from datetime import  datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=128)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice_text