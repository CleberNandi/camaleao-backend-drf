from django.urls import path
from django.views.generic import RedirectView
from .views import home


app_name = "chameleon"

urlpatterns = [
    path('', RedirectView.as_view(url='/home/')),
    path('home/', home, name='home'),
]
