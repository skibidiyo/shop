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


