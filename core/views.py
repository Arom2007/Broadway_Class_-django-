from django.shortcuts import render, redirect
from .models import Student, Menu
def students(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        address = request.POST.get("address")
        Student.objects.create(name=name, email=email, age=age, address=address)
        return redirect('students')

    students = Student.objects.all()  # [obj1, obj2, obj3]
    return render(request, template_name='core/students.html', context={"students": students, "title": "Students"})


def menu(request):
    menu = Menu.objects.all()

    return render(request, template_name='core/menu.html', context={"menu": menu, "title": "Food Menu", "menu_active": "active"})


