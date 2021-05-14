

from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('count/',views.count, name = 'count'),
    path('eggs/', views.eggs),
    path('proton/', views.proton)
]
