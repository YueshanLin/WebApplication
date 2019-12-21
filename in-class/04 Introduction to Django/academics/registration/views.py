from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

# Imports the Item class
from shared_todo_list.models import *


def register(request):
    all_items = Item.objects.all()

    return render(request, 'register.html', {'items':all_items})


def add_student(request):
    errors = []  # A list to record messages for any errors we encounter.

    # Adds the new item to the database if the request parameter is present
    if not 'item' in request.POST or not request.POST['item']:
        errors.append('You must enter an item to add.')
    else:
        new_item = Item(text=request.POST['item'])
        new_item.save()

    # Sets up data needed to generate the view, and generates the view
    items = Item.objects.all()
    context = {'items': items, 'errors': errors}
    return render(request, 'register.html', context)


def add_course(request):
    errors = []  # A list to record messages for any errors we encounter.

    # Adds the new item to the database if the request parameter is present
    if not 'item' in request.POST or not request.POST['item']:
        errors.append('You must enter an item to add.')
    else:
        new_item = Item(text=request.POST['item'])
        new_item.save()

    # Sets up data needed to generate the view, and generates the view
    items = Item.objects.all()
    context = {'items': items, 'errors': errors}
    return render(request, 'register.html', context)
