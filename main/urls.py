from django.urls import path
from main.views import show_main, create_food_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, add_food_entry_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_food
from main.views import delete_food
from main.views import create_food_flutter

app_name = 'main'


urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-food-entry', create_food_entry, name='create_food_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-food/<uuid:id>', edit_food, name='edit_food'),
    path('delete/<uuid:id>', delete_food, name='delete_food'),
    path('create-food-entry-ajax', add_food_entry_ajax, name='add_food_entry_ajax'),
    path('create-flutter/', create_food_flutter, name='create_food_flutter'),

]   