# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Choice_q
from TestModel.models import Essay_q
from django.http import JsonResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# 数据库操作
def testdb_choice_table(request):
    return render(request, "layui_choice_table.html")
    #choice_queryset = Choice_q.objects.all()
    #return render(request, "layui_choice_table.html", {"choice_queryset": choice_queryset})

def testdb_essay_table(request):
    return render(request, "layui_essay_table.html")
    #choice_queryset = Choice_q.objects.all()
    #return render(request, "layui_choice_table.html", {"choice_queryset": choice_queryset})

# 接收post请求

# 分页展示选择题数据
@csrf_exempt
def get_essay_data(request):
    essay_queryset = Essay_q.objects.all()
    data = []
    count = 0
    for essay_item in essay_queryset:
        count = count + 1
        data_item = {
            'id': essay_item.id,
            'question': essay_item.question,
            'answer': essay_item.answer,
            'point': essay_item.point
        }
        data.append(data_item)

    pageIndex = request.GET.get('curr', 1)
    pageSize = request.GET.get('nums', 10)


    start = (int(pageIndex) - 1) * int(pageSize)  # 数据起始位置
    end = int(pageIndex) * int(pageSize) # 数据终止位置
    if end >= count:
        end = count - 1

    data_show = []
    for x in range(start ,end):
        data_item = data[x]
        data_show.append(data_item)

    context = {
        "code": 0,
        "msg": "",
        "count": count,  # 所有数据数量
        "data": data_show  # 需要查询出来数据
    }
    return JsonResponse(context, safe=False)

# 分页展示选择题数据
@csrf_exempt
def get_choice_data(request):
    choice_queryset = Choice_q.objects.all()
    data = []
    count = 0
    for choice_item in choice_queryset:
        count = count + 1
        data_item = {
            'id': choice_item.id,
            'content': choice_item.content,
            'choice_a': choice_item.choice_a,
            'choice_b': choice_item.choice_b,
            'choice_c': choice_item.choice_c,
            'choice_d': choice_item.choice_d,
            'true_answer': choice_item.true_answer,
            'point': choice_item.point
        }
        data.append(data_item)

    pageIndex = request.GET.get('curr', 1)
    pageSize = request.GET.get('nums', 10)


    start = (int(pageIndex) - 1) * int(pageSize)  # 数据起始位置
    end = int(pageIndex) * int(pageSize) # 数据终止位置
    if end >= count:
        end = count - 1

    data_show = []
    for x in range(start ,end):
        data_item = data[x]
        data_show.append(data_item)

    context = {
        "code": 0,
        "msg": "",
        "count": count,  # 所有数据数量
        "data": data_show  # 需要查询出来数据
    }
    return JsonResponse(context, safe=False)
