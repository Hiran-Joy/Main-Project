from django.urls import path
from Employee import views
app_name = 'Employee'





urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),

    path("profile/",views.profile,name="profile"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path("changepassword/",views.changepassword,name="changepassword"),

    path("viewsalary/",views.viewsalary,name="viewsalary"),
    path("viewattendence/",views.viewattendence,name="viewattendence"),
    path("leaverequest/",views.leaverequest,name="leaverequest"),

    path("complaints/",views.complaints,name="complaints"),

]
