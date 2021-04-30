from django.urls import path
from .views import home


app_name = "chameleon"

urlpatterns = [
    path('home/', home, name='home'),
]
