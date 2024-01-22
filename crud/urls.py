from django.urls import path
from .views import classroom, delete_classroom, students, delete_student, update_student, update_classroom, student_profile
urlpatterns = [
    path('classroom/', classroom, name='classroom'),
    path('delete-classroom/<int:id>/', delete_classroom, name='delete_classroom'),
    path('update-classroom/<int:id>/', update_classroom, name='update_classroom'),
    path('student/', students, name='crud_students'),
    path('student-profile/', student_profile, name='student_profile'),
    path('delete-student/<int:id>/', delete_student, name='delete_student'),
    path('update-student/<int:id>/', update_student, name='update_student'),

]
