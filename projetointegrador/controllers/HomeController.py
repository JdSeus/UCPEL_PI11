from django.shortcuts import render, redirect

class HomeController():
    def index(request):
        """
        "When the user visits the home page, render the home/index.html template."
        
        The first line of the function is a decorator. A decorator is a special syntax that modifies the
        behavior of a function. In this case, the decorator tells Django that this function is a view
        
        :param request: This is the request object that is sent to the view
        :return: The index.html file is being returned.
        """
        return render(request, 'home/index.html')