from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def index(request):
    return render(request,'login_form/index.html')


def join_view(request):
    return render(request,'login_form/join_form.html')

def join(request):
    new_user_id = request.POST['member_id']
    Member(member_id = new_user_id).save()

    new_user_pw = request.POST['password']
    Member(password=new_user_pw).save()

    new_user_name = request.POST['name']
    Member(name=new_user_name).save()

    new_user_age = request.POST['age']
    Member(age=new_user_age).save()

    return HttpResponseRedirect(reverse('index'))







