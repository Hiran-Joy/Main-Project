from django.urls import path
from Admin import views
app_name = "Admin"

urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),


    path('hr/',views.hr,name="hr"),
    path('deletehr/<int:id>',views.deletehr,name="deletehr"),

    path('admin/',views.admin,name="admin"),
    path('deleteadmin/<int:id>',views.deleteadmin,name="deleteadmin"),
    path('editadmin/<int:id>',views.editadmin,name="editadmin"),

    path("viewcomplaint/",views.viewcomplaint,name="viewcomplaint"),
    path("reply/<int:id>",views.reply,name="reply"),
    path("replyedcomplaint/",views.replyedcomplaint,name="replyedcomplaint")
]