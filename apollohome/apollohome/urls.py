from django.contrib import admin
from django.urls import include, path
from professionals.views import dashboard_view, professionalCreate_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name='home'),
    path('create-profissional/', professionalCreate_view)
]
