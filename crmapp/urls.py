from django.contrib import admin
from django.urls import path ,include
from crmapp import views

urlpatterns = [

    path('', views.index, name='index'),

    path(r'account/', views.AccountAPIView.as_view(), name='account-list'),
    path(r'contacts/', views.ContactAPIView.as_view(), name='contact-list'),
    path(r'activities/', views.ActivityAPIView.as_view(), name='activity-list'),
    path(r'activitystatuses/', views.ActivityStatusAPIView.as_view(), name='activity-status-list'),
    path(r'contactsources/', views.ContactSourceAPIView.as_view(), name='contact-source-list'),
    path(r'contactstatuses/', views.ContactStatusAPIView.as_view(), name='contact-status-list')
]
