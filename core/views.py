from django.shortcuts import render
from .models import Student, Menu
def students(request):
    students = Student.objects.all()  # [obj1, obj2, obj3]
    classes = [
        {"Name": "one", "section": "A"},
        {"Name": "two", "section": "B"},
        {"Name": "three", "section": "C"},
        {"Name": "four", "section": "D"},
        {"Name": "five", "section": "E"}
    ]
    return render(request, template_name='core/students.html', context={"students": students, "classes": classes,
                                                                        "title": "Students"})


def menu(request):
    menu = Menu.objects.all()

    return render(request, template_name='core/menu.html', context={"menu": menu, "title": "Food Menu"})


