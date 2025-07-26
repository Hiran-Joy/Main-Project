from django.shortcuts import render,redirect
from datetime import date
from .models import tbl_user
from django.contrib import messages
from Admin.models import *
from Guest.models import *
from HR.models import *
from User.models import *
# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get("txt_email")
        password = request.POST.get("txt_password")
        usercount = tbl_user.objects.filter(user_email=email, user_password=password).count()
        admincount = tbl_admin.objects.filter(admin_email=email, admin_password=password).count()
        hrcount = tbl_hr.objects.filter(hr_email=email, hr_password=password).count()
        employeecount = tbl_employee.objects.filter(employee_email=email, employee_password=password).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=email, user_password=password)
            request.session["uid"] = user.id
            return redirect("User:user_profile")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=email, admin_password=password)
            request.session["aid"] = admin.id
            return redirect("Admin:homepage")
        elif hrcount > 0:
            hr = tbl_hr.objects.get(hr_email=email, hr_password=password)
            request.session["hrid"] = hr.id
            return redirect("HR:homepage")
        elif employeecount > 0:
            employee = tbl_employee.objects.get(employee_email=email, employee_password=password)
            request.session["eid"] = employee.id
            return redirect("Employee:homepage")
        else:
            return render(request, 'Guest/Login.html', {"error": "Invalid Email or Password"})
    else:
        return render(request, 'Guest/Login.html')

def index(request):
    return render(request, 'Guest/Index.html')

def view_recruitments(request):
    current_date = date.today()
    jobs = tbl_recruitment.objects.filter(
        recruitment_lastdate__gte=current_date
    ).order_by('-recruitment_date')
    
    context = {
        'jobs': jobs,
        'today': current_date
    }
    return render(request, 'Guest/view_recruitment.html', context)

def user_registration(request):
    if request.method == 'POST':
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        # contact = request.POST.get("txt_contact")
        # address = request.POST.get("txt_address")
        password = request.POST.get("txt_password")
        photo = request.FILES.get("txt_photo")
        # resume = request.FILES.get("txt_resume")

        # Duplicate Email Check (optional)
        if tbl_user.objects.filter(user_email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('Guest:userregister')

        tbl_user.objects.create(
            user_name=name,
            user_email=email,
            # user_contact=contact,
            # usre_address=address,
            user_password=password,
            user_photo=photo,
            # user_resume=resume
        )
        messages.success(request, "User registered successfully.")
        return redirect('Guest:userregister')
    
    users = tbl_user.objects.all()
    return render(request, 'Guest/user_registration.html', {'users': users})





