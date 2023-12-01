from django.urls import path
from . import views
urlpatterns = [
   path('', views.pon),
   path('pasha', views.otl)
]