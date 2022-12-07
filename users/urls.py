from django.urls import path

from .views import MainView, UserLogoutView


urlpatterns = [
    path('my-fruit-shop', MainView.as_view(), name='main'),
    path('logout', UserLogoutView.as_view(), name='logout'),
]
