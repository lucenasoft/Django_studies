from django.urls import path
from . import views
#  HTTP REQUEST

    # HTTP REQUEST
urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe) #home
]
