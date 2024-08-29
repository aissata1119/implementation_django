from django.shortcuts import redirect, render
from .forms import *
from .models import teacher


# Create your views here.

def index(request):
    teachers = teacher.objects.all()

    
    context={
        'teachers':teachers
    }
    return render(request, "teacher/index.html",context)

def edit(request):
    return render(request, "teacher/edit.html")

def add_teacher(request):
    if request.method == "POST":
        print(request.POST)
        form = teacherForM(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('teacher:index')
    else:
        form = teacherForM()

    form = teacherForM()
    context = {'form': form}
    return render(request, "teacher/add.html", context)
def update(request, id):

    teacher_id = teacher.objects.get(id=id)
    form = teacherForM(instance=teacher_id)
    
    if request.method == "POST":
        form = teacherForM(request.POST, instance=teacher_id)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')
    context = {'form':form}

    return render(request, 'teacher/edit.html', context)

def delete(request, id):

    teacher_id = teacher.objects.get(id = id)
    teacher_id.delete()
    return redirect ('teacher:index')

    

