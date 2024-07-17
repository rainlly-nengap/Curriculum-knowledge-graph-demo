# models.py
from django.db import models


class Login_user(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class User_Info(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_grade = models.CharField(max_length=255)
    user_classes = models.CharField(max_length=255)
    user_birthday = models.CharField(max_length=255)
    user_home = models.CharField(max_length=255)
    user_hobby = models.CharField(max_length=255)
    user_province = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_region = models.CharField(max_length=255)
    user_gender = models.CharField(max_length=3)
    user_sign = models.CharField(max_length=3)