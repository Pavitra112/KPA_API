from django.urls import path
from . import views

urlpatterns = [
    path('api/forms/wheel-specifications', views.wheel_spec_api, name='wheel-spec'),
]