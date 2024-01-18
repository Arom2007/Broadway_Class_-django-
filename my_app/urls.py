from django.urls import path
from .views import home1, template_home, template_home2, template_about_me, index, root_page

urlpatterns = [
    path("home/", template_home),
    path("new_home/", template_home2),
    path("aboutme/", template_about_me, name="portfolio"),
    path('index/', index),
    path('', root_page, name="root_page"),

]
