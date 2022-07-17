from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexdef,name='index'),
    path('about',views.aboutdef,name='about'),
    path('contacts',views.contactsdef,name='contacts'),
    path('home',views.homedef,name='home'),
    path('login',views.logindef,name='login'),
    path('baabtra',views.baabtra,name='baabtra')

]