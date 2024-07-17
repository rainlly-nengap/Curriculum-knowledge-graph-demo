# -*- coding: utf-8 -*-

from django.shortcuts import render

# 展示菜单页
def show_list(request):
    return render(request, "list.html")