"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from datetime import datetime
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from portal.app import views, forms

urlpatterns = [
    path('dashboard/login/', views.Accounts.Login.as_view(), name='login'),
    path('dashboard/', views.Dashboard.Index.as_view(), name='dashboard'),

    # Account
    path('dashboard/account/delete/<str:id>', views.Accounts.Delete.as_view()),
    path('dashboard/account/save/<str:id>', views.Accounts.Save.as_view()),
    path('dashboard/account/save/', views.Accounts.Save.as_view()),
    path('dashboard/accounts/', views.Accounts.Index.as_view()),

    # Students
    path('dashboard/student/delete/<str:id>', views.Students.Delete.as_view()),
    path('dashboard/student/save/<str:id>', views.Students.Save.as_view()),
    path('dashboard/student/save/', views.Students.Save.as_view()),
    path('dashboard/students/', views.Students.Index.as_view()),

    # Semester Routes
    path('dashboard/semester/delete/<str:id>', views.Semesters.Delete.as_view(), name='semester-delete'),
    path('dashboard/semester/save/<str:id>', views.Semesters.Save.as_view(), name='semester-save'),
    path('dashboard/semester/save/', views.Semesters.Save.as_view(), name='semester-save'),
    path('dashboard/semesters/', views.Semesters.Index.as_view(), name='semesters'),

    # Role Routes
    path('dashboard/role/delete/<str:id>', views.Roles.Delete.as_view()),
    path('dashboard/role/save/<str:id>', views.Roles.Save.as_view()),
    path('dashboard/role/save/', views.Roles.Save.as_view()),
    path('dashboard/roles/', views.Roles.Index.as_view()),

    # University Routes
    path('dashboard/university/delete/<str:id>', views.Universities.Delete.as_view(), name='du'),
    path('dashboard/university/save/<str:id>', views.Universities.Save.as_view(), name='su'),
    path('dashboard/university/save/', views.Universities.Save.as_view(), name='su'),
    path('dashboard/universities/', views.Universities.Index.as_view(), name='universities'),

    path('contact/', views.Home.Contact.as_view(), name='contact'),
    path('about/', views.Home.About.as_view(), name='about'),
    path('500/', views.Errors.Err500.as_view(), name='500'),
    path('', views.Home.Index.as_view(), name='home'),
]

# path('admin/', admin.site.urls),

# path('signin/',
#      LoginView.as_view
#      (template_name='login.html',
#       authentication_form=forms.BootstrapAuthenticationForm,
#       extra_context={
#           'title': 'Log in',
#           'year': datetime.now().year,
#       }
#       ),
#      name='signin'),
