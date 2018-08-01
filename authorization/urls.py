from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',auth_views.login, name='login'), # Stran na katero oddaš POST request da se logiraš
    url('logout/$', auth_views.logout, {'next_page': '/login'}, name="logout"),
]


"""
The URLs provided by auth are:

account/login/ [name='login']
account/logout/ [name='logout']
account/password_change/ [name='password_change']
account/password_change/done/ [name='password_change_done']
account/password_reset/ [name='password_reset']
account/password_reset/done/ [name='password_reset_done']
account/reset/<uidb64>/<token>/ [name='password_reset_confirm']
account/reset/done/ [name='password_reset_complete']

"""