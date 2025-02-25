from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
     path('admin/', admin.site.urls),
    path('download/', book_list, name='book_list'),
    path('', home,name='home'),
]
