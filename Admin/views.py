from django.shortcuts import render,redirect
from .models import tbl_hr
from HR.models import *
from Admin.models import *
from Employee.models import *
# Create your views here.

def homepage(request):
    return render(request,"Admin/HomePage.html")

def hr(request):
    hr = tbl_hr.objects.all()
    if request.method == 'POST':
        tbl_hr.objects.create(hr_name=request.POST.get('txt_name'),hr_email=request.POST.get('txt_email'),hr_password=request.POST.get('txt_password'),hr_photo=request.FILES.get("txt_photo"))
        return redirect("Admin:hr")
    else:
        return render(request, 'Admin/HR_registration.html', {'hr': hr})

def deletehr(request, id):
    tbl_hr.objects.get(id=id).delete()
    return redirect('Admin:hr')

def admin(request):
    admin = tbl_admin.objects.all()
    if request.method == 'POST':
        tbl_admin.objects.create(admin_name=request.POST.get('txt_name'),admin_email=request.POST.get('txt_email'),admin_password=request.POST.get('txt_password'))
        return redirect("Admin:admin")
    else:
        return render(request, 'Admin/Admin_registration.html', {'admin': admin})

def deleteadmin(request, id):
    tbl_admin.objects.get(id=id).delete()
    return redirect('Admin:admin')

def editadmin(request, id):
    admin = tbl_admin.objects.get(id=id)
    if request.method == 'POST':
        admin.admin_name = request.POST.get('txt_name')
        admin.admin_email = request.POST.get('txt_email')
        admin.admin_password = request.POST.get('txt_password')
        admin.save()
        return redirect('Admin:admin')
    else:
        return render(request, 'Admin/Admin_registration.html', {'editadmin': admin})

def viewcomplaint(request):
    hr=tbl_hr.objects.all()
    employee=tbl_employee.objects.all()
    hrcomplaint = tbl_complaint.objects.filter(complaint_status=0,hr__in=hr)
    employeecomplaint = tbl_complaint.objects.filter(complaint_status=0,employee__in=employee)
    print(employeecomplaint)
    return render(request,"Admin/ViewComplaint.html",{"hrcomplaint":hrcomplaint,'employeecomplaint':employeecomplaint})

def reply(request, id):
    if request.method == "POST":
        complaint = tbl_complaint.objects.get(id=id)
        complaint.complaint_status = 1
        complaint.complaint_reply = request.POST.get("txt_reply")
        complaint.save()
        return render(request,"Admin/Reply.html",{"msg":"Reply Sent"})
    else:
        return render(request,"Admin/Reply.html")

def replyedcomplaint(request):
    hr=tbl_hr.objects.all()
    employee=tbl_employee.objects.all()
    hrcomplaint = tbl_complaint.objects.filter(complaint_status=1,hr__in=hr)
    employeecomplaint = tbl_complaint.objects.filter(complaint_status=1,employee__in=employee)
    print(employeecomplaint)
    return render(request,"Admin/ReplyedComplaint.html",{"hrcomplaint":hrcomplaint,'employeecomplaint':employeecomplaint})

def hr_registration(request):
    if request.method == 'POST':
        # Check if email already exists
        email = request.POST.get('txt_email')
        if tbl_hr.objects.filter(hr_email=email).exists():
            messages.error(request, "This email is already in use. Please use a different one.")
            return render(request, 'hr_registration.html')

        # Proceed with saving HR if email is unique
        new_hr = tbl_hr(
            hr_name=request.POST.get('txt_name'),
            hr_email=email,
            hr_password=request.POST.get('txt_password'),
            hr_contact=request.POST.get('txt_contact'),
            hr_photo=request.FILES.get('txt_photo')
        )
        new_hr.save()
        messages.success(request, "HR has been registered successfully.")
        return redirect('some_view')  # Redirect after successful registration

    return render(request, 'hr_registration.html')