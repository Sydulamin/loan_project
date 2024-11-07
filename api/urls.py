from django.urls import path



from . import views

urlpatterns = [
    path('wing-one/', views.Wing_One_API_View.as_view(), name='wing-one'),
    path('wing-one-create/', views.Wing_One_Create_API_View.as_view(), name='wing-one-create'),

    path('login/', views.LoginApi.as_view(), name='api-login'),
    path('register/', views.UserRegisterApi.as_view(), name='api-register'),
]