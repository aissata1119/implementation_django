from django.shortcuts import get_object_or_404, redirect, render
from .forms import userForm
# from .models import user  
from django.contrib.auth.models import User

def index(request):
    users = User.objects.all()  
    context = {
        'users': users
    }
    return render(request, "users/index.html", context)

def add_user(request):
    if request.method == "POST":
        user_name = request.POST.get('username','')
        user_pass =request.POST.get('password','')
        if not user_name or not user_pass:
            return render(request, "users/add.html")
        user=User(username=user_name)
        user.save()
        user.password=user_pass
        user.set_password(user.password)
        user.save()
    #     form = userForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('users:index')  
    # else:
    #     form = userForm()

    # context = {'form': form}
    return render(request, "users/add.html")

def update_user(request,id):
    user_instance = get_object_or_404(User, id=id) 
    if request.method == "POST":
        form = userForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = userForm(instance=user_instance)

    context = {'form': form, 'user': user_instance}
    return render(request, "users/update.html", context)

    

