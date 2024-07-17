# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from LoginModel.models import Login_user
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render

# 展示菜单页
def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

def find_user(request):
    request.encoding = 'utf-8'
    if request.GET['username'] and request.GET['password']:
        usn = request.GET['username']
        psw = request.GET['password']
        users = Login_user.objects.all()
        message = '<script>alert("用户名或密码错误")</script>'
        for user in users:
            if user.username == usn and user.password == psw:
                request.session['username'] = usn
                return render(request, "list.html")
        messages.warning(request, '用户名或密码错误')
        return render(request, "login.html")

def add_user(request):
    request.encoding = 'utf-8'
    if request.GET['username'] and request.GET['password1'] and request.GET['password2']:
        usn = request.GET['username']
        psw1 = request.GET['password1']
        psw2 = request.GET['password2']
        if psw1 == psw2:
            user = Login_user(username=usn, password=psw1)
            user.save()
            return render(request, "login.html")
        messages.warning(request, '两次输入密码不一致')
        return render(request, "register.html")