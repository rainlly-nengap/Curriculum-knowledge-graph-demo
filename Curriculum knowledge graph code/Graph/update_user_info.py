# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from LoginModel.models import Login_user
from LoginModel.models import User_Info
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render

def update_user_info(request):
    request.encoding = 'utf-8'
    u_username = request.session.get('username', '')
    u_grades = request.GET['u_grades']
    u_class = request.GET['u_class']
    u_date = request.GET['u_date']
    u_home = request.GET['u_home']
    u_password = request.GET['u_password']
    u_interest = request.GET['u_interest']
    u_province = request.GET['u_province']
    u_city = request.GET['u_city']
    u_region = request.GET['u_region']
    u_gender = request.GET['u_gender']
    u_sign = request.GET['u_sign']

    Users = User_Info.objects.all()
    flag = 0
    for user in Users:
        if user.username == u_username:
            flag = 1
            break
    if flag == 1:
        User_Info.objects.filter(username=u_username).update(user_grade=u_grades)
        User_Info.objects.filter(username=u_username).update(user_classes=u_class)
        User_Info.objects.filter(username=u_username).update(user_birthday=u_date)
        User_Info.objects.filter(username=u_username).update(user_home=u_home)
        User_Info.objects.filter(username=u_username).update(password=u_password)
        User_Info.objects.filter(username=u_username).update(user_hobby=u_interest)
        User_Info.objects.filter(username=u_username).update(user_province=u_province)
        User_Info.objects.filter(username=u_username).update(user_city=u_city)
        User_Info.objects.filter(username=u_username).update(user_region=u_region)
        User_Info.objects.filter(username=u_username).update(user_gender=u_gender)
        User_Info.objects.filter(username=u_username).update(user_sign=u_sign)
    else:
        user = User_Info(username=u_username,
                          password=u_password,
                          user_grade=u_grades,
                          user_classes=u_class,
                          user_birthday=u_date,
                          user_home=u_home,
                          user_hobby=u_interest,
                          user_province=u_province,
                          user_city=u_city,
                          user_region=u_region,
                          user_gender=u_gender,
                          user_sign=u_sign
                          )
        user.save()
    messages.warning(request, '保存成功')
    return render(request, "user_table.html")