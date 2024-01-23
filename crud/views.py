from django.shortcuts import render, redirect
from .models import ClassRoom, Student, StudentProfile

def classroom(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.create(name=name)
        return redirect('classroom')

    classrooms = ClassRoom.objects.all()
    return render(request, template_name='crud/classroom.html', context={"classrooms": classrooms, "classroom_active": "active"})


def delete_classroom(request, id):
    clroom = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        clroom.delete()
        return redirect('classroom')
    return render(request, template_name="crud/delete_classroom.html", context={"classroom": clroom})


def update_classroom(request, id):
    classroom = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.filter(id=id).update(name=name)
        return redirect('classroom')
    return render(request, template_name="crud/update_classroom.html", context={"classroom": classroom})


def students(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        address = request.POST.get("address")
        classroom_id = request.POST.get("classroom")
        Student.objects.create(name=name, email=email, age=age, address=address, classroom_id=classroom_id)
        return redirect('crud_students')

    students = Student.objects.all()  # [obj1, obj2, obj3]
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='crud/student.html',
                  context={"students": students, "title": "Students", "classrooms": classrooms, "student_active": "active"})



def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect('crud_students')
    return render(request, template_name="crud/delete_student.html", context={"student": student})


def update_student(request, id):
    student = Student.objects.get(id=id)
    classrooms = ClassRoom.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        classroom_id = request.POST.get("classroom")
        Student.objects.filter(id=id).update(name=name, age=age, email=email, address=address, classroom_id=classroom_id)
        return redirect('crud_students')
    return render(request, template_name="crud/update_student.html", context={"student": student, "classrooms": classrooms})


def student_profile(request):
    profiles = StudentProfile.objects.all()
    students = Student.objects.all()
    if request.method == "POST":
        student_id = request.POST.get("student")
        phone = request.POST.get("phone")
        roll = request.POST.get("roll")
        pp = request.FILES.get("pp")
        sp = StudentProfile.objects.create(student_id=student_id, phone=phone, roll_no=roll)
        if pp:
            sp.profile_picture = pp
            sp.save()
        return redirect("student_profile")
    return render(request, template_name="crud/student_profile.html", context={"profiles": profiles,
                                                                               "students": students, "profile_active": "active"})


def delete_student_profile(request, id):
    profiles = StudentProfile.objects.get(id=id)
    if request.method == "POST":
        profiles.delete()
        return redirect('student_profile')
    return render(request, template_name="crud/delete_student_profile.html", context={"profiles": profiles})


def update_student_profile(request, id):
    profiles = StudentProfile.objects.get(id=id)
    if request.method == "POST":
        phone = request.POST.get("phone")
        roll = request.POST.get("roll")
        StudentProfile.objects.filter(id=id).update(phone=phone, roll_no=roll)
        return redirect('student_profile')
    return render(request, template_name="crud/update_student_profile.html", context={"profiles": profiles})


def detail_profile(request, id):
    profile = StudentProfile.objects.get(id=id)

    return render(request, template_name="crud/detail_profile.html", context={"profile": profile})