"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from PlaystylePicker import views
from PlaystylePicker.views import ReactAppView
from django.conf.urls.static import static
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required, user_passes_test

admin_only_view = user_passes_test(lambda u: u.is_authenticated and u.is_staff)(ReactAppView.as_view())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', include("PlaystylePicker.urls")),
    path('api/',include("PlaystylePicker.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', ReactAppView.as_view(), name='react_app'),  # React app route
    
    # Restrict /details to admin users
    path('createbuild/', admin_only_view, name='react_admin_only'),
]

# Serve images folder from React build at /images/
urlpatterns += static(
    '/images/',
    document_root=os.path.join(settings.BASE_DIR, 'PlaystylePicker', 'frontend', 'build', 'images')
)