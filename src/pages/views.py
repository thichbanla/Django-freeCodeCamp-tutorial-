from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context = {        
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": [1, 2, 45]
    }
    return render(request, 'about.html', my_context)