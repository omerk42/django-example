# django-example

\-/ to clone this rep

> git clone https://github.com/omerk42/django-example.git

1- install python

- lunix
> sudo apt-get install python3
- windows
> https://www.youtube.com/watch?v=ZRbirvsDQ-I&ab_channel=GeekyScript

~ check if python is installed 

- lunix 
> python3 --version
- windows
> python   ^should show python version^

2- create virtual envoirment

- lunix
> python3 -m venv env
- windows 
> python3 -m venv env

3- activate virtual envoirment

- lunix
> . env/bin/activate
- windows
> env\scripts\activate
* if error occur in powershell
1- run powershell as admin
2- > Set-ExecutionPolicy remoteSigned
3- type A
restart powershell

4- install django 

- lunix
> pip install django
- windows
> pip install django

5- create new django project

> django-admin startproject djangoProject

6- create database

> python3 manage.py migrate

7- runserver

> python3 manage.py runserver

8- create new django app

> python3 manage.py startapp djangoApp

9- add django app to the setting 
```
'appname.apps.AppnameConfig',
```
10- create first view 

```
from django.http import HttpResponse
def homepage(request):
 return HttpResponse("<h1> this homepage </h1>")
```

11- create urls

$ from django.urls import path
$ from . import views

$ urlpatterns = [
$    path('', views.homepage , name='home')
$ ]	

12- config app urls in project urls

$ path('', include('appname.urls')),	

13- create tamplates

create folder name templates

14- create static 

1- create folder name static 
2- load static in html

$ {% load static %} 
$
$ <link rel="stylesheet" href="{% static 'css/w3.css' %}">

<img src="{% static 'img/anchor.png' %}">

<img src="{% static 'img/cup.png' %}">

14- use django template lang

1- create blocs

{% block title %}
     any title you want
{% endblock title %}

2- create new html file in template folder

3- extend base html

{% extends 'urBaseHtmlFile.html' %}

4- change blocks as you like

15- models

1- create app models

2- add models to the admin

from .models import Contact

admin.site.register(Contact)

3- migrate database

> python3 manage.py makemigrations

> python3 manage.py migrate

4- create superuser

> python3 manage.py createsuperuser

5- access model via admin

6- edit model to be more readable

def __str__(self):
        return self.title

7- edit admin to be more useful

class ContactAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    ordering = ('date',)
    search_fields  = ('title','email')  
    
16 - forms 

1- create forms.py

from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['date']   

2- add form to the view 

form = ContactForm()    

,{'form':form}

3- add form to template

<div class="w3-row-padding w3-padding-64 w3-container">
    <div class="w3-content">
        <table>
            {{ form.as_table }}
        </table>    
    </div>
</div>

<td> <input type="submit" value="submit" > </td>

<form action="" method="post" novalidate>

{% csrf_token %}     

4- take input in view

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanx , we recevid your message ')
        else:
            messages.warning(request, str(form.errors)) 

5- show messages in tamplate

  {% for message in messages %}
  {% if message.tags == 'success' %}
  <div class="w3-panel w3-green w3-center" style="padding:30px 5px"> 
    <h3> {{ message }} </h3>
  </div> 
  {% else %}
  <div class="w3-panel w3-red w3-center" style="padding:30px 5px"> 
    <h3> {{ message }} </h3>
  </div>
  {% endif %} 
  {% endfor %}            
                      
