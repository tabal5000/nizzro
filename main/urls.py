from django.conf.urls import url
from django.urls import path, include
from . import views as main_views

urlpatterns = [
    path('',main_views.MainPage, name="main"),
    path('create', main_views.Create, name="create_computer"),
    url(r'^computer/(?P<pk>\d+)/$', main_views.Delete, name="delete_computer"),
    url(r'^computer/edit/(?P<pk>\d+)/$', main_views.Edit_Computer, name="edit_computer"),
]