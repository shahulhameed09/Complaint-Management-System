from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.contrib import messages
from ..forms import register

# Create your views here.    
    
def logins(request):

    if request.method=="POST":
        username=request.POST.get('names')
        password=request.POST.get('pass')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user_type = user.profile.user_type
            if user_type == 'admin':
                return redirect('/admin')
                
            elif user_type == 'officer':
                return redirect('/counter')
            
            elif user_type == 'user':
                return redirect('/user_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('/')
        else:
            messages.error(request,'Username Or Password Is Incorrect')
            return redirect('/')

    return render(request,'Auths/logins.html')
    
def user_register(request):
    if request.method == "POST":
        form=register(request.POST)
        if form.is_valid():
            types=form.save(commit=False)
            types.user_type = 3
            types.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account has been created for '+user)
            return redirect('/')
        else:
            messages.error(request, form.errors.get('username'))
    form = register()
    context={'form':form}
    return render(request,'Auths/user_register.html',context)

def officer_register(request):
    if request.method == "POST":
        form=register(request.POST)
        if form.is_valid():
            types=form.save(commit=False)
            types.user_type = 2
            types.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account has been created for '+user)
            return redirect('/')
        else:
            messages.error(request, form.errors.get('username'))
    form = register()
    context={'form':form}
    return render(request,'auths/officer_register.html',context)

# def logouts(request):
#     logout(request)
#     return redirect('/')

def add_staff_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_staff')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            # user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            # user.staffs.address = address
            # user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('add_staff')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_staff')