from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    my_title = "Hello here"
    return render(request, "home.html", {"title": my_title})

def about_page(request):
    my_title = "About Page"
    return render(request, "about.html", {"title": my_title})

def contact_page(request):
    my_title = "Contact Page"
    return render(request, "hello_world.html", {"title": my_title})

def manually_page():
    #Handle templates "manually". Only for academic purpouse
    my_title = "Hello there..."
    context = {"title": my_title}
    template_name = "title.txt"
    template_object = get_template(template_name)
    rendered_string = template_object.render(context)
    return render(request, "hello world", {"title": rendered_string}) #load a text located in file title.txt 
#