from django.urls import path
from .views import HomeView, ClassRoomView, StudentView, ClassRoomUpdateView, StudentUpdateView, ClassRoomDeleteView, StudentDeleteView


urlpatterns = [
    path('classroom/', ClassRoomView.as_view(), name="classbased_classroom"),
    path('classroom-update/<int:pk>/', ClassRoomUpdateView.as_view(), name="classbased_classroom_update"),
    path('classroom-delete/<int:pk>/', ClassRoomDeleteView.as_view(), name="classbased_classroom_delete"),
    path('student/', StudentView.as_view(), name='classbased_student'),
    path('student-update/<int:pk>/', StudentUpdateView.as_view(), name="classbased_student_update"),
    path('student-delete/<int:pk>/', StudentDeleteView.as_view(), name="classbased_student_delete"),
    path('', HomeView.as_view(), name='classbased_home')
]

