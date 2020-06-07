from django.shortcuts import render
from .models import User

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


def register(request):
    print("Got Post Info....................")
    name_from_register = request.POST['name']
    email_from_register = request.POST['email']
    context = {
        "current_user_name": name_from_register,
        "current_user_email": email_from_register
    }
    # new_user = User.objects.create(first_name)
    # print(new_user)
    return render(request, "index.html", context)
