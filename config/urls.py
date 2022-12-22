"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import TemplateView


"""=============Swagger docs============="""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

swagger_view = get_schema_view(
    openapi.Info(
        title="ASHERMovies",
        default_version='v1',
        description="ASHERMovies API"
    ),
    public=True
)
"""======================================"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', swagger_view.with_ui('swagger', cache_timeout=0)),
    path('', include('review.urls')),
    path('', include('main.urls')),
    path('account/', include('checkaccount.urls')),
    path('accounts/', include('allauth.urls')),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)