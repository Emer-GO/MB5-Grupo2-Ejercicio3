from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db.models import Q


# --- LOGIN ---
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student_list')
    else:
        form = LoginForm()
    return render(request, 'students/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# --- CRUD ESTUDIANTES ---
@login_required
def student_list(request):
    q = request.GET.get("q", "")  # recibe el texto de búsqueda
    students = Student.objects.all()
    if q:
        students = students.filter(
            Q(nombre__icontains=q) |
            Q(apellido__icontains=q) |
            Q(carrera__icontains=q)
        )
    return render(request, 'students/student_list.html', {
        'students': students,
        'q': q
    })

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})

def index(request):
    return render(request, 'students/index.html')


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario en la BD
            return redirect("login")  # Redirige al login
    else:
        form = UserCreationForm()
    return render(request, "students/register.html", {"form": form})