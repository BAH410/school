from django.shortcuts import render, redirect
from .models import Register_Student
from .forms import RegisterStudentForm
from django.contrib import messages

# Create your views here.


def home(request):
    students = Register_Student.objects.all()
    context = {
        'students': students}
    return render(request, 'school/index.html', context)


def register(request):
    form = RegisterStudentForm()
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    messages.success(request, 'Record save successfully')
    context = {'form': form}
    return render(request, 'school/add-student.html', context)


def UpdateRegister(request, pk):
    student = Register_Student.objects.get(id=pk)
    form = RegisterStudentForm(instance=student)
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'school/add-student.html', context)


def DeleteStudent(request, pk):
    student = Register_Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    context = {'student': student}
    return render(request, 'school/delete_student.html', context)
