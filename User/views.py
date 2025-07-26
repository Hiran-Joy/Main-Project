from django.shortcuts import render,redirect
from Guest.models import *
from datetime import date
from HR.models import *
from User.models import *
# Create your views here.


def user_profile(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    jobs = tbl_request.objects.filter(user=request.session["uid"])  # <-- Add this line

    return render(request, 'User/MyProfile.html', {
        'user': user,
        'jobs': jobs  # <-- And pass it here
    })

def view_recruitments(request):
    if not request.session.get("uid"):  # Or you can check request.user.is_authenticated
        return redirect('User:login')  # Redirect to login page if not logged in

    current_date = date.today()
    jobs = tbl_recruitment.objects.filter(
        recruitment_lastdate__gte=current_date
    ).order_by('-recruitment_date')
    
    context = {
        'jobs': jobs,
        'today': current_date
    }
    return render(request, 'User/view_recruitment.html', context)


def sendrequest(request, id):
    reqcount = tbl_request.objects.filter(user=request.session["uid"],recruitment=id).count()
    if reqcount > 0:
        return render(request,"User/view_recruitment.html",{"msg":"Already Request Send..."})
    else:
        tbl_request.objects.create(
            recruitment = tbl_recruitment.objects.get(id=id),
            user = tbl_user.objects.get(id=request.session["uid"])
        )
        return redirect("User:view_recruitments")

def myrequest(request):
    req = tbl_request.objects.filter(user=request.session["uid"])
    return render(request,"User/MyRequest.html",{"jobs":req})

def editprofile(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    if request.method == "POST":
        user.user_name = request.POST.get("txt_name")
        user.user_email = request.POST.get("txt_email")
        if request.FILES.get('txt_photo'):
            user.user_photo = request.FILES.get('txt_photo')
        user.save()
        return render(request,"User/MyProfile.html",{"msg":"Profile updated"})
    else:
        return render(request,"User/EditProfile.html",{"user":user})

def changepassword(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    if request.method == "POST":
        old_password = request.POST["txt_old"]
        new_password = request.POST["txt_new"]
        confirm_password = request.POST["txt_con"]
        if user.user_password == old_password:
            if new_password == confirm_password:
                user.user_password = new_password
                user.save()
                return render(request,"User/MyProfile.html",{"msg":"Password changed"})
            else:
                return render(request,"User/ChangePassword.html",{"msg":"Confirm Passwords do not match"})
        else:
            return render(request,"User/ChangePassword.html",{"msg":"Old Password is incorrect"})
    else:
        return render(request,"User/ChangePassword.html")
