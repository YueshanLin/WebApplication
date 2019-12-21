from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from blog.models import *
from blog.forms import *

from mimetypes import guess_type
from django.http import HttpResponse, Http404

from django.shortcuts import render, redirect, get_object_or_404

from django.core.mail import send_mail

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

import tzlocal  # $ pip install tzlocal

import datetime
import time
current_milli_time = lambda: int(round(time.time() * 1000))


def home(request):
    # Retrieve all posts
    posts = Post.objects.all().order_by('-time')
    context = {'posts': posts, 'userSelf': request.user}
    return render(request, 'Home.html', context)


def register(request):
    context = {}

    if request.method == 'GET':
        context['register_form'] = RegisterForm()
        return render(request, 'Register.html', context)

    register_form = RegisterForm(request.POST)
    context['register_form'] = register_form

    if not register_form.is_valid():
        return render(request, 'Register.html', context)

    # Send an email to the newly registered  to confirm the email address
    email_body = '-------------------------------Please confirm your email in order to successfully register-----------------------------'
    send_mail(subject='Verify your email address',
              message=email_body,
              from_email='yueshanl@andrew.cmu.edu',
              recipient_list=[register_form.cleaned_data['email']])

    new_user = User.objects.create_user(
                    username=register_form.cleaned_data['username'],
                    email=register_form.cleaned_data['email'],
                    first_name=register_form.cleaned_data['first_name'],
                    last_name=register_form.cleaned_data['last_name'],
                    password=register_form.cleaned_data['password'])
    new_user.save()
    new_userProfile = UserProfile(user=new_user,
                                  age=register_form.cleaned_data['age'])
    new_userProfile.save()

    user = authenticate(request,
                        username=register_form.cleaned_data['username'],
                        password=register_form.cleaned_data['password'])

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('forum')
    else:
        return HttpResponseRedirect('login')


def login_user(request):
    context = {}
    if request.method == 'GET':
        context['login_form'] = LoginForm()
        return render(request, 'Login.html', context)

    login_form = LoginForm(request.POST)
    context['login_form'] = login_form
    if not login_form.is_valid():
        return render(request, 'Login.html', context)

    user = authenticate(request,
                        username=login_form.cleaned_data['username'],
                        password=login_form.cleaned_data['password'])
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('forum')
    else:
        return HttpResponseRedirect('login')


@login_required
@ensure_csrf_cookie
@csrf_exempt
def forum(request):
    """
    context = {}
    # Post your comments
    if request.method == 'GET':
        context['PostForm'] = PostForm()
        # Retrieve all posts
        posts = Post.objects.all().order_by('-time')
        context = {'posts': posts, 'userSelf': request.user}
        return render(request, 'Forum.html', context)

    postForm = PostForm(request.POST)
    print("666666666666666666666666666666")
    context['PostForm'] = postForm
    if not postForm.is_valid():
        return render(request, 'Forum.html', context)

    post = Post(user=request.user, comment=postForm.cleaned_data['comment'])
    post.save()

    # Retrieve all posts
    posts = Post.objects.all().order_by('-time')
    context = {'posts': posts, 'userSelf': request.user}
    """
    print("form--------------------------------")
    context = {}
    return render(request, 'Forum.html', context)


@login_required
def profile(request, user_id):
    context = {}
    errors = []
    try:
        posts = Post.objects.filter(user__id=user_id).order_by('-time')
        user = User.objects.get(id=user_id)
        print(user.username)
        userProfile = UserProfile.objects.get(user__id=user_id)
        print('success', userProfile)
        context = {'user': user, 'posts': posts, 'userProfile': userProfile}
        return render(request, 'Profile.html', context)
    except:
        print('error')
        errors.append('User does not exist!')
        context = {'errors': errors, 'userSelf': request.user}
        return render(request, 'Profile.html', context)


@login_required
def edit(request):
    context = {}
    if request.method == 'GET':
        context['edit_form'] = EditForm()
        return render(request, 'Edit.html', context)

    edit_form = EditForm(request.POST, request.FILES)
    context['edit_form'] = edit_form

    if not edit_form.is_valid():
        return render(request, 'Edit.html', context)

    # Send an email to the newly registered  to confirm the email address
    email_body = '-------------------------------Please confirm your email in order to successfully register-----------------------------'
    send_mail(subject='Verify your email address',
              message=email_body,
              from_email='yueshanl@andrew.cmu.edu',
              recipient_list=[edit_form.cleaned_data['email']])

    userProfile = UserProfile.objects.get(user__id=request.user.id)
    userProfile.age = edit_form.cleaned_data['age']
    userProfile.profile = edit_form.cleaned_data['profile']
    userProfile.biography = edit_form.cleaned_data['biography']

    user = User.objects.get(id=request.user.id)
    user.first_name = edit_form.cleaned_data['first_name']
    user.last_name = edit_form.cleaned_data['last_name']
    user.email = edit_form.cleaned_data['email']
    user.password = edit_form.cleaned_data['password']
    user.save()
    userProfile.save()
    login(request, user)
    return HttpResponseRedirect('forum')


@login_required
def get_photo(request, user_id):
    userProfile = get_object_or_404(UserProfile, user__id=user_id)
    if not userProfile.profile:
        raise Http404

    content_type = guess_type(userProfile.profile.name)
    return HttpResponse(userProfile.profile, content_type=content_type)


@login_required
def follow(request, user_id):
    errors = []
    context = {}
    if UserProfile.objects.filter(user__id=request.user.id, userFollowed__id=user_id):
        errors.append('You have followed this user~')
        context['errors'] = errors
        context['PostForm'] = PostForm()
        # Retrieve all posts
        posts = Post.objects.all().order_by('-time')
        context = {'posts': posts, 'userSelf': request.user}
        return render(request, 'Forum.html', context)

    userProfile = UserProfile.objects.get(id=request.user.id)
    userProfile.userFollowed.add(User.objects.get(id=user_id))

    return HttpResponseRedirect(reverse_lazy('forum'))


@login_required
def unfollow(request, user_id):
    errors = []
    context = {}
    if not UserProfile.objects.filter(user__id=request.user.id, userFollowed__id=user_id):
        errors.append('You have not followed this user~')
        context['errors'] = errors
        context['PostForm'] = PostForm()
        # Retrieve all posts
        posts = Post.objects.all().order_by('-time')
        context = {'posts': posts, 'userSelf': request.user}
        return render(request, 'Forum.html', context)
    else:
        user_toRemove = User.objects.get(id=user_id)
        userProfile = UserProfile.objects.get(id=request.user.id)
        userProfile.userFollowed.remove(user_toRemove)
        return HttpResponseRedirect(reverse_lazy('forum'))


@login_required
def showFollow(request):
    context = {}

    # Post your comments
    if request.method == 'GET':
        context['PostForm'] = PostForm()
        # Retrieve all posts
        userProfile = UserProfile.objects.get(user=request.user)
        posts = Post.objects.filter(user__in=userProfile.userFollowed.all()).order_by('-time')
        context = {'posts': posts, 'userSelf': request.user}
        return render(request, 'FollowOnly.html', context)

    postForm = PostForm(request.POST)
    context['PostForm'] = postForm

    if not postForm.is_valid():
        return render(request, 'FollowOnly.html', context)

    post = Post(user=request.user, comment=postForm.cleaned_data['comment'])
    post.save()

    # Retrieve all posts of the "followees"
    userProfile = UserProfile.objects.get(user=request.user)

    posts = Post.objects.filter(user__in=userProfile.userFollowed.all()).order_by('-time')
    context = {'posts': posts, 'userSelf': request.user}
    return render(request, 'FollowOnly.html', context)


@login_required
def logout_user(request):
    logout(request)
    return render(request, 'Logout.html', {})


@csrf_exempt
def get_changes(request):
    """
    if 'time' in request.GET and request.GET['time']:
        # Converting the unix timestamp to readable time format
        time_temp = datetime.datetime.utcfromtimestamp(float(request.GET['time'])).strftime('%Y-%m-%d %H:%M:%S')
    else:
        time_temp = datetime.datetime.utcfromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')
    """

    if 'time' in request.GET and request.GET['time']:
        # Converting the unix timestamp to readable time format
        time_temp = datetime.datetime.fromtimestamp(float(request.GET['time']) + 1, tzlocal.get_localzone()).strftime('%Y-%m-%d %H:%M:%S')
    else:
        time_temp = datetime.datetime.fromtimestamp(float(0 + 1), tzlocal.get_localzone()).strftime('%Y-%m-%d %H:%M:%S')

    print("----------------------time when retrieve posts: should be less than the new post' time")
    print(request.GET['time'])
    print(time_temp)
    print('max time in post')
    print(time.mktime(datetime.datetime.strptime(Post.get_max_time(), "%Y-%m-%d %H:%M:%S").timetuple()))
    print(Post.get_max_time())
    print("max time in subPost")
    print(time.mktime(datetime.datetime.strptime(SubPost.get_max_time(), "%Y-%m-%d %H:%M:%S").timetuple()))
    print(SubPost.get_max_time())

    if SubPost.get_max_time() > time_temp:
        print("SubPost.get_max_time() > time_temp")
    else:
        print("SubPost.get_max_time() <= time_temp")

    posts = Post.objects.filter(time__gt=time_temp)
    subPosts = SubPost.objects.filter(time__gt=time_temp)
    if posts.exists():
        print("posts not empty")
    else:
        print("posts empty")

    if subPosts.exists():
        print("subPosts not empty")
    else:
        print("subPosts empty")



    # Retrieve the lastest time of a change
    # Converting string to unix timestamp
    # max_time_post_subPost = max(Post.get_max_time(), SubPost.get_max_time())
    max_time_post_subPost = max(Post.get_max_time(), SubPost.get_max_time())


    timestamp = time.mktime(datetime.datetime.strptime(max_time_post_subPost, "%Y-%m-%d %H:%M:%S").timetuple())

    # I do not render subPost according to the requirement
    context = {'timestamp': timestamp, 'posts': posts, 'subPosts': subPosts, 'messages': []}
    return render(request, 'posts.json', context, content_type='application/json')


@csrf_exempt
def add_post(request):

    if not 'comment' in request.POST or not request.POST['comment']:
        raise Http404
    else:
        newPost = Post(user=request.user, comment=request.POST['comment'])
        newPost.save()
        timestamp = time.mktime(newPost.time.timetuple())
        print("newPost time++++++++++++++++++++++++++++++++++")
        print(timestamp)

        context = {'timestamp': timestamp, 'posts': [], 'subPosts': [], 'messages': []}
        # return HttpResponse('')
        return render(request, 'posts.json', context, content_type='application/json')


@csrf_exempt
def add_subPost(request, postID):
    print("5-5-55-5-5-5-555555-5-5-")
    if 'comment' not in request.POST or not request.POST['comment']:
        raise Http404
    else:
        post = Post.objects.get(id=postID)
        newSubPost = SubPost(comment=request.POST['comment'], user=request.user, post=post)
        newSubPost.save()
        timestamp = time.mktime(newSubPost.time.timetuple())
        context = {'timestamp': timestamp, 'posts': [], 'subPosts': [], 'messages': []}
        return render(request, 'posts.json', context, content_type='application/json')
