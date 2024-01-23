from django.urls import path
from .views import (classroom, delete_classroom, students, delete_student, update_student, update_classroom,
                    student_profile, delete_student_profile, update_student_profile, detail_profile)
urlpatterns = [
    path('classroom/', classroom, name='classroom'),
    path('delete-classroom/<int:id>/', delete_classroom, name='delete_classroom'),
    path('update-classroom/<int:id>/', update_classroom, name='update_classroom'),
    path('student/', students, name='crud_students'),
    path('student-profile/', student_profile, name='student_profile'),
    path('delete-student-profile/<int:id>/', delete_student_profile, name='delete_student_profile'),
    path('update-student-profile/<int:id>/', update_student_profile, name='update_student_profile'),
    path('delete-student/<int:id>/', delete_student, name='delete_student'),
    path('update-student/<int:id>/', update_student, name='update_student'),
    path('detail-profile/<int:id>/', detail_profile, name='detail_profile')

]
