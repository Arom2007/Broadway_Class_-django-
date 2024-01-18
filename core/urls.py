from django.urls import path
from .views import students, menu

urlpatterns = [
    path('', students, name='students'),
    path('menu/', menu, name='menu')
]
