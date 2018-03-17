cfrom django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    path('event/<int:event_id>', views.event_view, name='event_view'),
    path('feed/', views.feed, name='feed')
]
