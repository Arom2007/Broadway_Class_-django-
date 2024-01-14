from django.urls import path
from .views import home1, template_home, template_home2

urlpatterns = [
    path('home1/', home1),
    path("ghar/", template_home),
    path("newghar/",template_home2)


]