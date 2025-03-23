"""
URL configuration for smartcard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from fetch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.load,name='load'),
    path('home', views.index,name='home'),
    path('uid', views.pwd),
    path('login_view', views.login_view,name='login_view'),
    path('logout_view', views.logout_view,name='logout_view'),
    path('download_docs', views.download_docs,name='download_docs'),
    path('download_information', views.download_information,name='download_information'),
    path('download_information_view', views.download_info_view,name='download_info_view'),
    path('download_reports', views.download_reports,name='download_reports'),
    path('upload_document', views.upload_document,name='upload_document'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
