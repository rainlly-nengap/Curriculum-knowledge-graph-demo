# models.py
from django.db import models

class Choice_q(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False)
    content = models.CharField(max_length=255)
    choice_a = models.CharField(max_length=255)
    choice_b = models.CharField(max_length=255)
    choice_c = models.CharField(max_length=255)
    choice_d = models.CharField(max_length=255)
    true_answer = models.CharField(max_length=255)
    point = models.CharField(max_length=255)

class Essay_q(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    point = models.CharField(max_length=255)



