from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def cars_view(request):
    return HttpResponse('Meus carros')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('cars/', cars_view),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)