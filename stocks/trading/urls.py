from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns=[
    path('', views.home, name = "home"),
    path('portfolio', views.portfolio, name = "portfolio"),
    path('buy', views.buy, name = "buy"),
    path('sell', views.sell, name = "sell"),
    path('transaction', views.transaction, name = "transaction")

]