from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")

def graph(request):
    return render(request, "graph.html")

def report(request):
    return render(request, "report.html")

def settings(request):
    return render(request, "settings.html")

def login(request):
    return render(request, "login.html")