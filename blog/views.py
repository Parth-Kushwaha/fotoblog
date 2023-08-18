from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from . import forms

@login_required
def home_page(request):
    return render(request, 'blog/home.html')

@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method=='POST':
        form=forms.PhotoForm(request.POST, request.FILES)
        photo=form.save(commit=False)
        photo.uploader= request.user
        photo.save()
        return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form':form})