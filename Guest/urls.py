from django.urls import path
from Guest import views
app_name = "Guest"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('',views.index,name="index"),
    path('view-recruitments/', views.view_recruitments, name='view_recruitments'),
    path('userregister/', views.user_registration, name='userregister'),

]