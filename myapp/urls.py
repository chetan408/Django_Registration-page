from django.views.generic import TemplateView

from . import views
from django.urls import path

urlpatterns = [
    path('',views.customer_details),
    path('search/', views.customer_search, name="search"),
]
