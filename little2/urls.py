from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cun/', cun, name='cun'),
    path('qu/', qu, name='qu'),
    path('cunkuan/', qu, name='cunkuan'),

]
