from django.urls import path
from . import views


urlpatterns = [
    path('Mail', views.SendMail.as_view(), name='mail'),
]