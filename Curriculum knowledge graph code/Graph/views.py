from django.http import HttpResponse
from django.shortcuts import render


def runoob(request):
  views_list = ['a','hello','b']
  return render(request, "runoob.html", {'item1':views_list[0],'item2':views_list[1],'item3':views_list[2]})
