from django.shortcuts import render, redirect

class HomeController():
    def index(request):
        return render(request, 'home/index.html')