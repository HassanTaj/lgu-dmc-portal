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
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
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