from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.gallery , name='gallery'),
    path('addphoto/', views.add , name='addphoto'),
    path('viewphoto/<str:pk>/', views.view , name='viewphoto'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

