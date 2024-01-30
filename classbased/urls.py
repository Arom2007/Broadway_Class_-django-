from django.urls import path
from .views import HomeView, ClassRoomView, StudentView


urlpatterns = [
    path('classroom/', ClassRoomView.as_view(), name="classbased_classroom"),
    path('student/', StudentView.as_view(), name='classbased_student'),
    path('', HomeView.as_view(), name='classbased_home')
]

