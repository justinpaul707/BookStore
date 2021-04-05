from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import UserCreationForm
# Create your views here.
def user_login(request):
    if request.method == 'GET':
        context = {}
        context["form"]=AuthenticationForm()
        return render(request,'accounts/login.html',context)
    elif request.method == 'POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            username =form.cleaned_data["username"]
            password =form.cleaned_data["password"]
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('book_home')
        else:
            context = {}
            context["form"]=form
            return render(request,'accounts/login.html',context)
            
def register(request):
    if request.method == 'GET':
        context={}
        context['form']=UserCreationForm()
        return render(request,'accounts/register.html',context)
    elif request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            user=form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect("accounts_login")
        else:
            context={}
            context['form']=form
            return render(request,'accounts/register.html',context)

def user_logout(request):
    logout(request)
    return redirect('accounts_login')
        
        
        
        
        


