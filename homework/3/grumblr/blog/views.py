from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# import Post
from blog.models import *


def register(request):
    errors = []
    context = {}
    completeInfo = True
    if 'username' not in request.POST or not request.POST['username']:
        errors.append('Must enter a username')
        completeInfo = False
    else:
        username = request.POST['username']

    if 'firstname' not in request.POST or not request.POST['firstname']:
        errors.append('Must enter a first name')
        completeInfo = False
    else:
        firstname = request.POST['firstname']

    if 'lastname' not in request.POST or not request.POST['lastname']:
        errors.append('Must enter a last name')
        completeInfo = False
    else:
        lastname = request.POST['lastname']

    if 'password' not in request.POST or not request.POST['password']:
        errors.append('Must enter the password ')
        completeInfo = False
    else:
        password = request.POST['password']

    if 'password_conf' not in request.POST or not request.POST['password_conf']:
        errors.append('Must enter the password confirmation')
        completeInfo = False
    else:
        password_conf = request.POST['password_conf']

    if completeInfo:
        if password != password_conf:
            errors.append('The passwords enters do not match!')
        else:
            user_other = User.objects.filter(username=username)
            if user_other:
                errors.append('Username already used before!')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password)
                user.save()
                return HttpResponseRedirect('login')

    context = {'errors': errors}
    return render(request, 'Register.html', context)


def login_user(request):
    errors = []
    context = {}
    completeInfo = True
    if 'username' not in request.POST or not request.POST['username']:
        errors.append('Must enter a username!')
        completeInfo = False
    else:
        username = request.POST['username']

    if 'password' not in request.POST or not request.POST['password']:
        errors.append('Must enter a password!')
        completeInfo = False
    else:
        password = request.POST['password']

    if completeInfo:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('forum')
        else:
            errors.append('user does not exist')

    context = {'errors': errors}
    return render(request, 'Login.html', context)


def forum(request):
    errors = []
    context = {}
    comment = ''
    # Post your comments
    if 'comment' not in request.POST or not request.POST['comment']:
        errors.append('Please post a comment')
    else:
        comment = request.POST['comment']
        newPost = Post(user=request.user, comment=comment)
        newPost.save()

    # Retrieve all posts
    posts = Post.objects.all().order_by('-time')

    context = {'posts': posts, 'errors': errors, 'userSelf': request.user}
    return render(request, 'Forum.html', context)


def profile(request, user_id):
    context = {}
    errors = []
    try:
        posts = Post.objects.filter(user__id=user_id).order_by('-time')
        user = User.objects.get(id=user_id)
        context = {'user': user, 'posts': posts, 'userSelf': request.user}
        return render(request, 'Profile.html', context)
    except:
        errors.append('User does not exist!')
        context = {'errors': errors, 'userSelf': request.user}
        return render(request, 'Profile.html', context)


def home(request):

    return render(request, 'Home.html', {})
