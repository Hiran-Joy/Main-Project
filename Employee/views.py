from django.shortcuts import render
from HR.models import  *
from Employee.models import  *
from datetime import datetime
# Create your views here.

def homepage(request):
    return render(request,"Employee/Homepage.html")

def profile(request):
    employee = tbl_employee.objects.get(id=request.session["eid"])
    return render(request,"Employee/MyProfile.html",{"employee":employee})

def editprofile(request):
    employee = tbl_employee.objects.get(id=request.session["eid"])
    if request.method == "POST":
        employee.employee_name = request.POST.get("txt_name")
        employee.employee_email = request.POST.get("txt_email")
        employee.employee_contact = request.POST.get("txt_contact")
        employee.employee_address = request.POST.get("txt_address")
        if request.FILES.get('txt_photo'):
            employee.employee_photo = request.FILES.get('txt_photo')
        employee.save()
        return render(request,"Employee/MyProfile.html",{"msg":"Profile updated"})
    else:
        return render(request,"Employee/EditProfile.html",{"employee":employee})

def changepassword(request):
    employee = tbl_employee.objects.get(id=request.session["eid"])
    if request.method == "POST":
        old_password = request.POST["txt_old"]
        new_password = request.POST["txt_new"]
        confirm_password = request.POST["txt_con"]
        if employee.employee_password == old_password:
            if new_password == confirm_password:
                employee.employee_password = new_password
                employee.save()
                return render(request,"Employee/MyProfile.html",{"msg":"Password changed"})
            else:
                return render(request,"Employee/ChangePassword.html",{"msg":"Confirm Passwords do not match"})
        else:
            return render(request,"Employee/ChangePassword.html",{"msg":"Old Password is incorrect"})
    else:
        return render(request,"Employee/ChangePassword.html")

def viewsalary(request):
    emp = tbl_salary.objects.filter(employee=request.session["eid"])
    if request.method == "POST":
        dates = request.POST.get("txt_date")
        date_object = datetime.strptime(dates, "%Y-%m")
        emp = tbl_salary.objects.filter(salary_date__month=date_object.month,employee=request.session["eid"])
        return render(request, 'Employee/ViewSalary.html', {'emp':emp})
    return render(request, 'Employee/ViewSalary.html', {'emp':emp})

def viewattendence(request):
    emp = tbl_attendence.objects.filter(employee=request.session["eid"])
    if request.method == "POST":
        dates = request.POST.get("txt_date")
        emp = tbl_attendence.objects.filter(attendence_date=dates,employee=request.session["eid"])
        return render(request, 'Employee/View_attendence.html', {'emp':emp})
    return render(request, 'Employee/View_attendence.html', {'emp':emp})

def leaverequest(request):
    emp = tbl_leave.objects.filter(employee=request.session["eid"])
    if request.method == "POST":
        tbl_leave.objects.create(
            employee = tbl_employee.objects.get(id=request.session["eid"]),
            leave_content = request.POST.get('txt_content')
        )
        return render(request, 'Employee/LeaveRequest.html', {'msg':"Leave Request Send Successfully"})
    return render(request, 'Employee/LeaveRequest.html', {'emp':emp})

def complaints(request):
    complaint = tbl_complaint.objects.filter(employee=request.session["eid"])
    if request.method == "POST":
        tbl_complaint.objects.create(complaint_title=request.POST.get("txt_title"),complaint_content=request.POST.get("txt_content"),employee=tbl_employee.objects.get(id=request.session["eid"]))
        return render(request,"Employee/Complaint.html",{"msg":"Complaint Send Sucessfully.."})
    else:
        return render(request,"Employee/Complaint.html",{"complaint":complaint})

