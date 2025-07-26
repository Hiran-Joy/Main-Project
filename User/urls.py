from django.urls import path
from User import views
app_name = "User"

urlpatterns = [

path('myprofile/', views.user_profile, name='user_profile'),
path('view_recruitments/', views.view_recruitments, name='view_recruitments'),
path('sendrequest/<int:id>', views.sendrequest, name='sendrequest'),
path('myrequest/', views.myrequest, name='myrequest'),
path("editprofile/",views.editprofile,name="editprofile"),
path("changepassword/",views.changepassword,name="changepassword"),




   
]