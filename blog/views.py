from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from . import forms,models


@login_required
def home_page(request):
    photos=models.Photo.objects.all()
    blog=models.Blog.objects.all()
    return render(request, 'blog/home.html',context={'photos':photos,'blog':blog})

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
    
@login_required
def blog_photo_upload(request):
    blog_form=forms.BlogForm()
    photo_form=forms.PhotoForm()
    if request.method=='POST':
        blog_form=forms.BlogForm(request.POST)
        photo_form=forms.PhotoForm(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            blog= blog_form.save(commit=False)
            blog.author=request.user
            blog.save()

            photo= photo_form.save(commit=False)
            photo.uploader= request.user
            photo.save()

            return redirect('home')
    context={
        'blog_form':blog_form,
        'photo_form':photo_form
    }
    return render(request, 'blog/blog_photo_upload.html', context)

@login_required
def view_blog(request,blog_id):
    blog=forms.BlogForm(models.Blog, id=blog_id)
    return render(request, 'blog/view_blog.html',context={'blog':blog})

            
