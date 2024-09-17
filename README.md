# Shop Project

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).
- Make sure Python and Django is already installed
- Create a new directory with the name RORONOA and enter it.
- Inside the directory, open the vscode terminal.
- Create a virtual environment by running the following command.
    ```
    python -m venv env
   ```
- Activate the virtual environment with the following command.
    ```
    env\Scripts\activate
    ```
- Create a requirements.txt file and add some dependencies.
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
- Install the dependencies with the following command.
    ```
    pip install -r requirements.txt
    ```
- Create a Django project named skibishop with the following command:
    ```
    django-admin startproject skibishop .
    ```
- Include the following two strings in the ALLOWED_HOSTS list within settings.py for deployment purposes:
    ```
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ```
- Run the Django server with the following command:
    ```
    python manage.py runserver
    ```
- Create a new application called main by running the following command:
    ```
    python manage.py startapp main
    ```
- Open the settings.py file inside the skibishop project directory. Add 'main' to the INSTALLED_APPS variable as shown below.
    ```
    INSTALLED_APPS = [
    ...,
    'main'
    ]
    ```
- Create a new directory named templates inside the main application directory.
- Inside the templates directory, create a new file named main.html and fill the main.html file with the following code
    ```
    <h1>SKIBI SHOP</h1>

    <h5>Name: </h5>
    <p>{{ name }}</p> <!-- Change according to your name -->
    <h5>Class: </h5>
    <p>{{ class }}</p> <!-- Change according to your class -->
    ```
- Open the models.py file in the main application directory.

    Fill the models.py file with the following code:
    from django.db import models
    ```
    class product(models.Model):
        name = models.CharField(max_length=255)
        mood_intensity = models.IntegerField()
        description = models.TextField()
    ```
- After creating the model, run migrations.
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
- Open the views.py file located in the main application file.
- Add the show_main function.
    ```
    from django.shortcuts import render

    def show_main(request):
    context = {
        'name': 'Anindiyo Banu',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)
    ```
- Modify the main.html template to display data that has been retrieved from the model.
    ```
    <h1>SKIBI SHOP</h1>

    <h5>Name: </h5>
    <p>{{ name }}</p> <!-- Change according to your name -->
    <h5>Class: </h5>
    <p>{{ class }}</p> <!-- Change according to your class -->
    ```
- Configuring the URL Routing for the main application. Create a urls.py file in the main directory.

- Paste the following content inside urls.py:
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
- Open the urls.py file inside of the skibishop project directory, import the include function.
    ```
    from django.urls import path, include
    ```
- Add the following URL route to direct to the main view within the urlpatterns variable
    ```
    urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
    ]
    ```
- Perform deployment to PWS so that it can be accessed by others via the Internet

- Create a new project labeled as skibishop
- On the settings.py file of the Django project that you have just created, add the PWS deployment URL to the ALLOWED_HOSTS field.
    ```
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "anindiyo-banu-skibishop.pbp.cs.ui.ac.id"]
    ```
- Do a git add, commit, and push change to the GitHub repository you have created.

## Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file

![alt text](image.png)
The user sends a request to the web server.
The request is routed through urls.py to the appropriate view in views.py.
The view may communicate with models.py to access or update data.
The view renders the data into an HTML template.
Finally, the response is sent back to the user.

## Explain the use of git in software development!
Git plays a critical role in software development by providing a powerful, distributed version control system that supports collaboration, branching, code reviews, and historical tracking of changes. It enables teams to work together efficiently, manage large projects, and maintain the integrity of the codebase throughout the development lifecycle.

## In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?
Django is an excellent starting point for learning software development because it provides a balanced mix of simplicity, structure, and functionality. It allows to quickly build full-stack web applications, teaches them best practices, and offers a supportive community. Additionally, as a Python-based framework, it makes transitioning to more complex development tasks smooth, ensuring that developers have both a strong foundation and room to grow their skills.

## Why is the Django model called an ORM?
Django's model is called an ORM because it allows developers to work with relational databases using object-oriented programming techniques, hiding the complexities of SQL behind an easy-to-use Python API. This not only speeds up development but also makes database operations more secure, maintainable, and scalable. Django’s ORM abstracts the database layer so that developers can focus on writing business logic without worrying about the specifics of SQL syntax or database management.


## Explain why we need data delivery in implementing a platform.
Data delivery ensures that information moves smoothly and securely between parts of a platform. It helps everything work together, provides fast responses, handles more users without slowing down, keeps data safe, and makes the platform easy to use.

## In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
JSON is more popular than XML because it’s simpler, smaller, faster, and works better with modern web technologies like JavaScript. It’s easier to read, write, and process, making it a better fit for most applications today, while XML is more complex and suited for specialized tasks.

##  Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.
The is_valid() method in Django forms checks if the submitted data is correct and follows the form's rules. If the data is valid, it returns True, allowing further actions like saving data. If not, it returns False, helping display error messages. It's important for ensuring data accuracy and preventing errors.

## Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?
The csrf_token in Django forms protects against CSRF attacks, where attackers trick users into submitting harmful requests. Without it, malicious users could exploit the form to perform actions like changing data or transferring money without the user's knowledge. The token ensures that form submissions are from your website and not from attackers.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).
- Create a directory templates in the main directory (root folder) and create a new HTML file named base.html. Create the base.html file with the following code:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
- Open the settings.py file in the project directory (skibishop) and find the line that contains the TEMPLATES variable. Adjust the code with the following code to make the base.html file detected as a template file
```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Add this line
        'APP_DIRS': True,
        ...
    }
]
...
```

 - Create a new file in the main directory with the name forms.py so that it can receive Product datas.
 ```
 from django.forms import ModelForm
from main.models import FoodEntry

class FoodEntryForm(ModelForm):
    class Meta:
        model = FoodEntry
        fields = ["name", "price", "description",]
```
- Changing the Primary Key From Integer to UUID. Add these lines to the models.py file on the main/ subdirectory
```
from django.db import models
import uuid

class FoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
```

- Open the views.py file in the main directory and add from django.shortcuts import render, redirect. Create a new function to add a product.
```
def create_food_entry(request):
    form = FoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_food_entry.html", context)
```
- Change the show_main function to the following
```
def show_main(request):
    food_entries = FoodEntry.objects.all()

    context = {
        'name': 'Anindiyo Banu',
        'class': 'PBP KKI',
        'food_entries': food_entries
    }

    return render(request, "main.html", context)
```
- Open the views.py file in the main directory and add these imports.
```
from django.http import HttpResponse
from django.core import serializers
```
- Insert the following functions into views.py.
```
def show_xml(request):
data = Product.objects.all()
return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

- Open urls.py and import the following:
from main.views import show_main, create_food_entry show_xml, show_json, show_xml_by_id, show_json_by_id

- Add the URL path to the urlpatterns variable in the urls.py file
```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-food-entry', create_food_entry, name='create_food_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

## Access the four URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.

XML
![alt text](image-1.png)

JSON
![alt text](image-2.png)

XML by id
![alt text](image-3.png)

JSON by id
![alt text](image-4.png)