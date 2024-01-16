from django.urls import path
from .views import home1, template_home, template_home2, template_about_me

urlpatterns = [
    path('', home1),
    path("home/", template_home),
    path("new_home/", template_home2),
    path("aboutme/", template_about_me)

]
