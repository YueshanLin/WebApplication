"""grumblr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.home, name='home'),
    path('login', blog.views.login_user, name='login'),
    path('register', blog.views.register, name='register'),
    path('forum', blog.views.forum, name='forum'),
    path('profile/<int:user_id>', blog.views.profile, name='profile'),
    path('edit', blog.views.edit, name='edit'),
    path('photo/<int:user_id>', blog.views.get_photo, name='photo'),
    path('follow/<int:user_id>', blog.views.follow, name='follow'),
    path('unfollow/<int:user_id>', blog.views.unfollow, name='unfollow'),
    path('showFollow', blog.views.showFollow, name='showFollow'),
    path('logout', blog.views.logout_user, name='logout'),
    path('get_changes', blog.views.get_changes, name='get_changes'),
    # path('getChanges/(?P<time>.+)$', blog.views.get_changes, name='get_changes'),
    path('add_post', blog.views.add_post, name='add_post'),
    path('add_subPost/<int:postID>', blog.views.add_subPost, name='add_subPost'),
]
