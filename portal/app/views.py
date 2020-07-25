"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.http import *
from django.views.generic.base import View

from lib.uow.UnitOfWorkModule import *


def home(request):
    uow: UnitOfWork = request.uow
    uow.users_repo.get_all()
    assert isinstance(request, HttpRequest)
    return render(request, template_name='client/home.html')


def dashboard(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'dashboard/home.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def login(request):
    assert isinstance(request, HttpRequest)
    return render(request=request,
                  template_name='dashboard/signin.html')
