"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.http import *
from django.views.generic.base import View

from lib.uow.UnitOfWorkModule import *


# Client side Home
class Home(object):
    """
        This Class is just a wrapper where we can group all the views that will be used
        for clients view handling class based views
    """

    class Index(View):
        def get(self, request):
            uow: UnitOfWork = request.uow
            uow.seed(doseed=(uow.roles_repo.get_all() == 0))
            assert isinstance(request, HttpRequest)
            return render(request, template_name='client/home.html', context={
                'title': 'Home',
            })

    class About(View):
        def get(self, request):
            assert isinstance(request, HttpRequest)
            return render(request, template_name='client/about.html', context={
                'title': 'About',
            })

    class Contact(View):
        def get(self, request):
            assert isinstance(request, HttpRequest)
            return render(request, template_name='client/contact.html', context={
                'title': 'Contact Us',
            })


# Accounts
class Accounts(object):
    class Login(View):
        def get(self, request):
            uow: UnitOfWork = request.uow
            assert isinstance(request, HttpRequest)
            return render(request=request, template_name='dashboard/signin.html', context={
                'title': 'Login',
                'universities': uow.universities_repo.get_all()
            })

        def post(self, request):
            uow: UnitOfWork = request.uow
            user: Account = uow.account_repo.get_by_username_or_password(uname=request.POST['uname'],
                                                                         pswd=request.POST['pswd'])
            if user is None:
                return HttpResponseRedirect(reverse('login') + '?loginfailed=true')

            return HttpResponseRedirect(reverse('dashboard'))

    class Logout(View):
        def get(self, request):
            return HttpResponseRedirect(reverse('home'))

    class Index(View):
        def get(self, request):
            uow: UnitOfWork = request.uow
            return render(request, template_name="dashboard/accounts.html", context={
                'title': 'Users',
                'list': uow.account_repo.get_all()
            })

    class Save(View):
        def get(self, request, id=None):
            uow: UnitOfWork = request.uow
            item = None
            if id is not None and id != '':
                item = uow.account_repo.get_by_id(id)
            return render(request, template_name="dashboard/account-form.html", context={
                'title': 'Users',
                'model': item,
                'roles': uow.roles_repo.get_all(),
                'unis': uow.universities_repo.get_all(),
                'students': uow.students_repo.get_all()
            })

        def post(self, request):
            try:
                uow: UnitOfWork = request.uow
                model: Account = Account(
                    id=request.POST['id'],
                    user_name=request.POST['user_name'],
                    email=request.POST['email'],
                    password=request.POST['password'],
                    email_confirmed=False,
                )

                if 'university_id' in request.POST:
                    model.university_id = request.POST['university_id']

                if 'role_id' in request.POST:
                    model.role_id = request.POST['role_id']

                if 'student_id' in request.POST:
                    model.student_id = request.POST['student_id']

                if model.id is not None and model.id != '':
                    uow.account_repo.update(model.id, model)
                else:
                    uow.account_repo.create(model)

                return HttpResponseRedirect(reverse('accounts'))
            except Exception as ex:
                return HttpResponseRedirect(reverse('500'))

    class Delete(View):
        def get(self, request, id):
            uow: UnitOfWork = request.uow
            if id is not None and id != '':
                uow.account_repo.delete(Account(id=id))
            return HttpResponseRedirect(reverse('accounts'))


# Roles
class Roles(object):
    class Index(View):
        def get(self, request):
            uow: UnitOfWork = request.uow
            return render(request, template_name="dashboard/roles.html", context={
                'title': 'Roles',
                'roles': uow.roles_repo.get_all()
            })

    class Save(View):
        def get(self, request, id=None):
            uow: UnitOfWork = request.uow
            item = None
            if id is not None and id != '':
                item = uow.roles_repo.get_by_id(id)

            return render(request, template_name="dashboard/role-form.html", context={
                'model': item
            })

        def post(self, request):
            try:
                uow: UnitOfWork = request.uow
                model: Role = Role(
                    id=request.POST['id'],
                    name=request.POST['role-name']
                )
                if model.id is not None and model.id != '':
                    uow.roles_repo.update(model.id, model)
                else:
                    uow.roles_repo.create(model)

                return HttpResponseRedirect(reverse('roles'))
            except Exception as ex:
                return HttpResponseRedirect(reverse('500'))

    class Delete(View):
        def get(self, request, id):
            uow: UnitOfWork = request.uow
            if id is not None and id != '':
                uow.semesters_repo.delete(University(id=id))
            return HttpResponseRedirect(reverse('universities'))


# Dashboard
class Dashboard(object):
    class Index(View):
        def get(self, request):
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'dashboard/home.html',
                {
                    'title': 'Dashboard',
                    'year': datetime.now().year,
                }
            )

    class SemesterList(View):
        def get(self, request):
            return render(request, 'dashboard/')


# Universities
class Universities(object):
    class Index(View):
        def get(self, request):
            uow: UnitOfWork = request.uow
            return render(request, template_name="dashboard/universities.html", context={
                'title': 'Universities',
                'unis': uow.universities_repo.get_all()
            })

    class Save(View):
        def get(self, request, id=None):
            uow: UnitOfWork = request.uow
            item = None
            if id is not None and id != '':
                item = uow.universities_repo.get_by_id(id)

            return render(request, template_name="dashboard/university-form.html", context={
                'model': item
            })

        def post(self, request):
            try:
                uow: UnitOfWork = request.uow
                model: University = University(
                    id=request.POST['id'],
                    name=request.POST['institute-name']
                )
                if model.id is not None and model.id != '':
                    uow.universities_repo.update(model.id, model)
                else:
                    uow.universities_repo.create(model)

                return HttpResponseRedirect(reverse('universities'))
            except Exception as ex:
                return HttpResponseRedirect(reverse('500'))

    class Delete(View):
        def get(self, request, id):
            uow: UnitOfWork = request.uow
            if id is not None and id != '':
                uow.universities_repo.delete(University(id=id))
            return HttpResponseRedirect(reverse('universities'))


# Semester
class Semesters(object):
    class Index(View):
        def get(self, request):
            uow: UnitOfWork = request.uow
            return render(request, template_name="dashboard/semesters.html", context={
                'title': 'Semesters',
                'list': uow.semesters_repo.get_all()
            })

    class Save(View):
        def get(self, request, id=None):
            uow: UnitOfWork = request.uow
            item = None
            if id is not None and id != '':
                item = uow.semesters_repo.get_by_id(id)

            return render(request, template_name="dashboard/semester-form.html", context={
                'model': item
            })

        def post(self, request):
            try:
                uow: UnitOfWork = request.uow
                model: Semester = Semester(
                    id=request.POST['id'],
                    number=request.POST['semester_number']
                )
                if model.id is not None and model.id != '':
                    uow.semesters_repo.update(model.id, model)
                else:
                    uow.semesters_repo.create(model)

                return HttpResponseRedirect(reverse('semesters'))
            except Exception as ex:
                return HttpResponseRedirect(reverse('500'))

    class Delete(View):
        def get(self, request, id):
            uow: UnitOfWork = request.uow
            if id is not None and id != '':
                uow.semesters_repo.delete(Semester(id=id))
            return HttpResponseRedirect(reverse('semesters'))


# Student
class Students(object):
    class Index(View):
        def get(self, request):
            uow: UnitOfWork = request.uow
            return render(request, template_name="dashboard/students.html", context={
                'title': 'Students',
                'list': uow.students_repo.get_all()
            })

    class Save(View):
        def get(self, request, id=None):
            uow: UnitOfWork = request.uow
            item = None
            if id is not None and id != '':
                item = uow.students_repo.get_by_id(id)

            return render(request, template_name="dashboard/student-from.html", context={
                'model': item
            })

        def post(self, request):
            try:
                uow: UnitOfWork = request.uow
                model: Student = Student(
                    id=request.POST['id'],
                    first_name=request.POST['f_name']
                )
                if model.id is not None and model.id != '':
                    uow.students_repo.update(model.id, model)
                else:
                    uow.students_repo.create(model)

                return HttpResponseRedirect(reverse('students'))
            except Exception as ex:
                return HttpResponseRedirect(reverse('500'))

    class Delete(View):
        def get(self, request, id):
            uow: UnitOfWork = request.uow
            if id is not None and id != '':
                uow.semesters_repo.delete(Student(id=id))
            return HttpResponseRedirect(reverse('students'))


# Results
class Results(object):
    class Index(View):
        def get(self, request):
            uow: UnitOfWork = request.uow
            return render(request, template_name="dashboard/results.html", context={
                'title': 'Results',
                'list': uow.student_results_repo.get_all()
            })

    class Save(View):
        def get(self, request, id=None):
            uow: UnitOfWork = request.uow
            item = None
            if id is not None and id != '':
                item = uow.students_repo.get_by_id(id)

            return render(request, template_name="dashboard/result-from.html", context={
                'model': item
            })

        def post(self, request):
            try:
                uow: UnitOfWork = request.uow
                model: StudentResult = StudentResult(
                    id=request.POST['id'],
                )
                if 'student_id' in request.POST:
                    model.student_id = request.POST['student_id']
                if 'semester_id' in request.POST['semester_id']:
                    model.semester_id = request.POST['semester_id']

                if 'res_path' in request.POST['res_path']:
                    model.res_path = request.POST['res_path']

                if model.id is not None and model.id != '':
                    uow.student_results_repo.update(model.id, model)
                else:
                    uow.student_results_repo.create(model)

                return HttpResponseRedirect(reverse('students'))
            except Exception as ex:
                return HttpResponseRedirect(reverse('500'))

    class Delete(View):
        def get(self, request, id):
            uow: UnitOfWork = request.uow
            if id is not None and id != '':
                uow.semesters_repo.delete(Student(id=id))
            return HttpResponseRedirect(reverse('students'))


# Errors
class Errors(object):
    class Err500(View):
        def get(self, request):
            return render(request, template_name="error/500.html")
