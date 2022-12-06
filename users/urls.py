from django.urls import path

from .views import TestView, UserLogoutView


urlpatterns = [
    path('my-fruit-shop', TestView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
]
