from django.urls import path
from django.contrib.auth.views import logout
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    path('event/<int:event_id>', views.event_view, name='event_view'),
    path('feed/', views.feed, name='feed'),
    path('create_event/', views.create_event, name='create_event'),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('setup/', views.setup, name="setup"),
    path('profile/<int:userid>', views.profile, name="profile")
]
