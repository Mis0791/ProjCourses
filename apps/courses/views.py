from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Course
from django.contrib.messages import error

def index(request):
    return render(request, 'courses/index.html', { "courses": Course.objects.all()})

def create(request):
    errors = Course.objects.validate(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else: 
        Course.objects.create(
            name=request.POST['name'],
            desc=request.POST['desc']
        )
    return redirect('/')

def confirm(request, courses_id):
    return render(request, 'courses/confirm.html', { "courses": Course.objects.get(id=courses_id)})

def delete(request, courses_id):
    Course.objects.get(id=courses_id).delete()
    return redirect('/')