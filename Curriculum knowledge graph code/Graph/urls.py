"""Graph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from . import views, testdb, neo4j, bar_list,login,update_user_info

urlpatterns = [
    #url(r'^$', views.hello),      #此时需要在浏览器中输入http://127.0.0.1:8000/
    #path('runoob/', views.runoob),
    url(r'^login/$', login.login_page), #此时需要在浏览器中输入http://127.0.0.1:8000/login
    url(r'^register/$', login.register_page), #此时需要在浏览器中输入http://127.0.0.1:8000/login
    url(r'login_request/', login.find_user),  # 登录请求路由
    url(r'register_request/', login.add_user),
    url(r'user_info_request/', update_user_info.update_user_info),
    url(r'^list/$', bar_list.show_list), #此时需要在浏览器中输入http://127.0.0.1:8000/list
    url(r'^testdb_c/$', testdb.testdb_choice_table),  #此时需要在浏览器中输入http://127.0.0.1:8000/testdb_c
    url(r'^testdb_e/$', testdb.testdb_essay_table),  #此时需要在浏览器中输入http://127.0.0.1:8000/testdb_e
    url(r'search_choice/', testdb.get_choice_data),  # 监听分页的路由
    url(r'search_essay/', testdb.get_essay_data),  # 监听分页的路由
    url(r'^neo4jdb_h/$', neo4j.show_graph_h_data), #此时需要在浏览器中输入http://127.0.0.1:8000/neo4jdb
    url(r'^neo4jdb_b/$', neo4j.show_graph_b_data), #此时需要在浏览器中输入http://127.0.0.1:8000/neo4jdb
    url(r'^neo4jdb_p/$', neo4j.show_graph_p_data), #此时需要在浏览器中输入http://127.0.0.1:8000/neo4jdb
    url(r'^user_table/$', neo4j.show_user_table), #此时需要在浏览器中输入http://127.0.0.1:8000/neo4jdb
]
