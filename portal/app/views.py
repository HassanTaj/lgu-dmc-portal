"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import *
from django.views.generic.base import View

from lib.uow.UnitOfWorkModule import *


class Home(object):
    """
        This Class is just a wrapper where we can group all the views that will be used
        for clients view handling class based views
    """

    class Index(View):
        def get(self, request):
            uow: UnitOfWork = request.uow
            uow.seed(doseed=True)
            assert isinstance(request, HttpRequest)
            return render(request, template_name='client/home.html')

    class About(View):
        def get(self, request):
            assert isinstance(request, HttpRequest)
            return render(request, template_name='client/about.html')


class Accounts(object):
    class Login(View):
        def get(self, request):
            uow: UnitOfWork = request.uow
            assert isinstance(request, HttpRequest)
            return render(request=request, template_name='dashboard/signin.html', context={
                'universities': uow.universities_repo.get_all()
            })

        def post(self, request):
            uow: UnitOfWork = request.uow
            user: Account = uow.account_repo.get_by_username_or_password(uname=request.POST['uname'],
                                                                         pswd=request.POST['pswd'])
            if user is None:
                return HttpResponseRedirect(reverse('login') + '?loginfailed=true')

            return HttpResponseRedirect(reverse('dashboard'))


class Dashboard(object):
    class Index(View):
        def get(self, request):
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'dashboard/home.html',
                {
                    'title': 'Home Page',
                    'year': datetime.now().year,
                }
            )