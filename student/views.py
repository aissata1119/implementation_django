from django.shortcuts import redirect, render
from .forms import *



# Create your views here.

def index(request):
    
    students = student.objects.all()

    context = {
        'students':students
    }
    return render(request, "student/index.html",context)



def add_student(request):
    context = {"title":"Ajouter un eleve"}

    if request.method == "POST":
        print(request.POST)
        form = studentForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('student:index')
        else:
            return render(request, "student/add.html")
        
    form = studentForm()
    
    context["form"] = form
   
    return render(request, "student/add.html", context)


def update(request, id):
    context = {"title":"Modifier un eleve"}

    student_id = student.objects.get(id = id)

    #form = studentForm(instance=student_id)
    
    if request.method == "POST":
        form = studentForm(request.POST, instance=student_id)
        if form.is_valid():
            form.save()
            return redirect('student:index')
        
    form = studentForm(instance = student_id)
    context["form"] = form

    return render(request, 'student/add.html', context)

    

def delete(request, id):

    student_id = student.objects.get(id = id)
    student_id.delete()
    return redirect ('student:index')