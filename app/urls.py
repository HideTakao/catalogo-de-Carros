from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, NewCarCreateView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)