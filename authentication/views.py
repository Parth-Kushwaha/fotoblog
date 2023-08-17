from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.shortcuts import render,redirect
from django.views.generic import View

from . import forms

# class based view
class LoginPage(View):
    form_class=forms.LoginForm
    template_name='authentication/login.html'

    def get(self,request):
        message=''
        form=self.form_class
        return render(request, self.template_name, context={'form':form, 'message': message})  

    def post(self,request):
        form= self.form_class(request.POST)
        
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],
                              password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                message='logged in'
                return redirect('home')
            else:
                message='Login Failed'

        return render(request, self.template_name, context={'form':form, 'message': message})

# function based view
def logout_user(request):
    logout(request)
    return redirect('login')

def login_form(request):
    message=''
    form = forms.LoginForm()
    if request.method=='POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user= authenticate(username= form.cleaned_data['username'],
                               password= form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message='Login Failed!'
    return render(request, 'authentication/login.html', context={'form':form, 'message': message})

def signUp(request):
    form=  forms.SignUpForm()
    if request.method=='POST':
        form=forms.SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form':form})

