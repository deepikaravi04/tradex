from django.urls import path
from . import views


urlpatterns = [
    path('', views.tradex_home, name="xhome"),

]