"""kin_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include

api_patterns = ([
                    url(r'^auth/', include('rest_auth.urls')),
                    url(r'^auth/register/', include('rest_auth.registration.urls')),
                ], 'api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns, namespace='api')),
    path('accounts/', include('allauth.urls')),  # new
    path('api/', include('kin_test_api.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
