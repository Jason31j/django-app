from django.shortcuts import render

# Create your views here.
def vista_login(request):
    return render(request, "login.html") 

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")