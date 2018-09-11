from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('edit/',views.editb,name='editb'),
    path('<int:pk>/edit/',views.edit,name='edit'),
]