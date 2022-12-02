from django.contrib import admin
from django.urls import path
from . import views as contact_views

urlpatterns = [
    path('contact/', contact_views.contact_view, name='contact'),
    path('contact/', contact_views.about, name='about')
]