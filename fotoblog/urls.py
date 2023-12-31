"""
URL configuration for fotoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
import authentication.views 
import blog.views

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True,
        ),name='login'),

    path('logout/',authentication.views.logout_user,name='logout'),
    path('home/',blog.views.home_page,name='home'),
    path('signup/',authentication.views.signUp,name='signup'),
    path('photo/upload/', blog.views.photo_upload,name='photo_upload'),
    path('photo-delete/<int:photo_id>',blog.views.delete_photo,name='photo-delete'),
    path('photo/profile/', authentication.views.profilePhoto,name='profile_photo'),
    path('createpost/', blog.views.blog_photo_upload,name='createpost'),
    path('viewblog/<int:blog_id>',blog.views.view_blog,name='view-blog'),
    path('viewblog/<int:blog_id>/edit', blog.views.edit_blog,name='editBlog'),
    path('photo/uploadmultiple',blog.views.create_multiple_photos, name='multiplePhotos')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    
