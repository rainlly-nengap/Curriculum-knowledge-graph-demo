import os
import json
import codecs
from django.shortcuts import render
from py2neo import Graph,Node,Relationship
#graph = Graph("http://localhost:7474/", auth=("neo4j", "neo4j_0336"),name="mygraph.db")
def show_graph_h_data(request):
  graph_title = "welcome"
  return render(request, "twitter-trolls-h.html")

def show_graph_b_data(request):
  graph_title = "welcome"
  return render(request, "twitter-trolls-b.html")

def show_graph_p_data(request):
  graph_title = "welcome"
  return render(request, "twitter-trolls-p.html")

def test_layui(request):
  return render(request,"layui_choice_table.html")

def show_user_table(request):
  username = request.session.get('username', '')
  return render(request,"user_table.html", {"username": username})
