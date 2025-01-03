from django.shortcuts import render, redirect 
from main.forms import FoodEntryForm
from main.models import FoodEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@login_required(login_url='/login')

def show_main(request):

    context = {
        'name': request.user.username,
        'class': 'PBP KKI',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_food_entry(request):
    form = FoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        food_entry = form.save(commit=False)
        food_entry.user = request.user
        food_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_food_entry.html", context)

def show_xml(request):
    data = FoodEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = FoodEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = FoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = FoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
         messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_food(request, id):
    food = FoodEntry.objects.get(pk = id)

    # Set food entry as an instance of the form
    form = FoodEntryForm(request.POST or None, instance=food)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_food.html", context)

def delete_food(request, id):
    # Get food based on id
    food = FoodEntry.objects.get(pk = id)
    # Delete food
    food.delete()
    # Return to home page
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_food_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    description = strip_tags(request.POST.get("description")) # strip HTML tags!
    price = request.POST.get("price")
    user = request.user

    new_food = FoodEntry(
        name=name, description=description,
        price = price,
        user=user
    )
    new_food.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_food_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_food = FoodEntry.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"]
        )

        new_food.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)