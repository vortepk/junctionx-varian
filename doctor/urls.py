from django.urls import path

from .views import MainPage

app_name = 'doctor'

urlpatterns = [
    path('', MainPage.as_view(), name='main_page')
]
