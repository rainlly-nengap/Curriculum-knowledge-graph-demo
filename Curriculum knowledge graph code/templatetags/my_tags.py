from django import template

register = template.Library()   #register的名字是固定的,不可改变

#利用装饰器 @register.filter 自定义过滤器。
@register.filter
def test(v1,v2):
    s = v1 + v2
    return s

#利用装饰器 @register.simple_tag 自定义标签
@register.simple_tag
def mytag(v1,v2,v3):
    s = v1 + v2 + v3
    return s

