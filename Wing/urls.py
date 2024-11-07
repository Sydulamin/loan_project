from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('wings', views.index, name='home'),
    path('update-wing/<int:pk>/', views.update_wing, name='update-wing'),
    path('wing/<int:pk>', views.wing_page, name='wing'),
]