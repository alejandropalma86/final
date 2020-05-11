"""appsolutions URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    #Patshs de Core
    path('', include('core.urls')),
    #Patshs de Services
    path('services/', include('services.urls')),
    #Patshs de Blog
    path('blog/', include('blog.urls')),
    #Patshs de Pages
    path('page/', include('pages.urls')),
    #Patshs de Contact
    path('contact/', include('contact.urls')),
    #Patshs de Vacancy
    path('vacancy/', include('vacancy.urls')),
    #Patshs de Account
    path('', include('account.urls')),
    #Paths del Admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
