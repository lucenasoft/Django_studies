from django.urls import path
from . import views
#  HTTP REQUEST

app_name = 'recipes'

    # HTTP REQUEST
urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe") #home
]
