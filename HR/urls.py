from django.urls import path
from HR import views
app_name = "HR"

urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),

    path("profile/",views.profile,name="profile"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path("changepassword/",views.changepassword,name="changepassword"),

    path('role/',views.role,name="role"),
    path('deleterole/<int:id>',views.deleterole,name="deleterole"),
    path('editrole/<int:id>',views.editrole,name="editrole"),

    path("employee/",views.employee,name="employee"),
    path("viewemployee/",views.viewemployee,name="viewemployee"),
    path("addattendence/<int:id>",views.addattendence,name="addattendence"),
    path("addsalary/<int:id>",views.addsalary,name="addsalary"),

    path("viewattendence/",views.viewattendence,name="viewattendence"),
    path("viewsalary/",views.viewsalary,name="viewsalary"),
    path("viewleaverequest/",views.viewleaverequest,name="viewleaverequest"),

    path("verifyleave/<int:id>/<int:status>",views.verifyleave,name="verifyleave"),
    
    path('content/', views.contentpage, name='contentpage'),
    path('delete/<int:content_id>/', views.deletecontent, name='deletecontent'),
    path('viewrequest/<int:id>/', views.viewrequest, name='viewrequest'),
    path('verifyreqest/<int:id>/<int:status>/<int:reqid>', views.verifyreqest, name='verifyreqest'),

    path('deleteemployee/<int:id>/', views.deleteemployee, name='deleteemployee'),

    path('delete_salary/<int:id>/', views.delete_salary, name='delete_salary'), 

    path("complaints/",views.complaints,name="complaints"),
    

]   