from django.urls import path
from .views import classroom, delete_classroom, students, delete_student
urlpatterns = [
    path('classroom/', classroom, name='classroom'),
    path('delete-classroom/<int:id>/', delete_classroom, name='delete_classroom'),
    path('student/', students, name='crud_students'),
    path('delete-student/<int:id>/', delete_student, name='delete_student')
]
