from django import forms
from crud.views import ClassRoom, Student


class ClassRoomModelForm(forms.ModelForm):
    class Meta:
        fields = ["name",]
        model = ClassRoom


class StudentForm(forms.ModelForm):
    class Meta:
        fields = ["name", "email", "age", "address", "classroom"]
        model = Student

