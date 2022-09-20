from django.urls import path

from recipes.views import home, contato, sobre
#  HTTP REQUEST

    # HTTP REQUEST
urlpatterns = [
    path('', home), #home
    path('sobre/', sobre), # /sobre/
    path('contato/', contato) # /contato/
]