from django.urls import path
from .import views

urlpatterns = [
    path('index',views.indexdef,name='index'),
    path('about',views.aboutdef,name='about'),
    path('contacts',views.contactsdef,name='contacts'),
    path('home',views.homedef,name='home')
]