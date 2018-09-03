from django.conf.urls import url
from django.urls import path, include
from . import views as main_views

urlpatterns = [
    path('',main_views.MainPageView, name="main_view"),
    path('syslists', main_views.SystemListsView, name="syslists_view"),
    url(r'^list_element/(?P<pk>\d+)/$', main_views.ListElementsDetailView, name="list_element_detail"),
    url(r'^processor', main_views.ProcessorView, name="processor_view"),
]