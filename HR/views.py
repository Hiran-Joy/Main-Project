from django.shortcuts import render,redirect
from datetime import date, datetime
from django.contrib import messages
from .models import tbl_recruitment, tbl_hr
from django.shortcuts import get_object_or_404, redirect
from HR.models import tbl_salary
from Admin.models import tbl_hr
from HR.models import *
from Admin.models import *
from Employee.models import *
from User.models import *

# Create your views here.

def homepage(request):
    return render(request,"HR/Homepage.html")

def profile(request):
    hr = tbl_hr.objects.get(id=request.session["hrid"])
    return render(request,"HR/MyProfile.html",{"hr":hr})

def editprofile(request):
    hr = tbl_hr.objects.get(id=request.session["hrid"])
    if request.method == "POST":
        hr.hr_name = request.POST.get("txt_name")
        hr.hr_email = request.POST.get("txt_email")
        hr.hr_contact = request.POST.get("txt_contact")
        if request.FILES.get('txt_photo'):
            hr.hr_photo = request.FILES.get('txt_photo')
        hr.save()
        return render(request,"HR/MyProfile.html",{"msg":"Profile updated"})
    else:
        return render(request,"HR/EditProfile.html",{"hr":hr})

def changepassword(request):
    hr = tbl_hr.objects.get(id=request.session["hrid"])
    if request.method == "POST":
        old_password = request.POST["txt_old"]
        new_password = request.POST["txt_new"]
        confirm_password = request.POST["txt_con"]
        if hr.hr_password == old_password:
            if new_password == confirm_password:
                hr.hr_password = new_password
                hr.save()
                return render(request,"HR/MyProfile.html",{"msg":"Password changed"})
            else:
                return render(request,"HR/ChangePassword.html",{"msg":"Confirm Passwords do not match"})
        else:
            return render(request,"HR/ChangePassword.html",{"msg":"Old Password is incorrect"})
    else:
        return render(request,"HR/ChangePassword.html")

def employee(request):
    role = tbl_role.objects.all()
    if request.method == 'POST':
        tbl_employee.objects.create(employee_name=request.POST.get("txt_name"),
                                employee_email=request.POST.get("txt_email"),
                                employee_password=request.POST.get("txt_password"),
                                employee_contact=request.POST.get("txt_contact"),
                                employee_address=request.POST.get("txt_address"),
                                employee_idnumber=request.POST.get("txt_empid"),
                                employee_photo=request.FILES.get("txt_photo"),
                                employee_proof=request.FILES.get("txt_proof"),
                                role=tbl_role.objects.get(id=request.POST.get("sel_role")))
        return render(request, 'HR/Employee.html',{"msg":"You Registred Sucessfully"})
    return render(request,"HR/Employee.html",{"role":role})

def role(request):
    role = tbl_role.objects.all()
    if request.method == 'POST':
        tbl_role.objects.create(role_name=request.POST.get('txt_name'))
        return redirect("HR:role")
    else:
        return render(request, 'HR/Role.html', {'role': role})

def deleterole(request, id):
    tbl_role.objects.get(id=id).delete()
    return redirect('HR:role')

def editrole(request, id):
    role = tbl_role.objects.get(id=id)
    if request.method == 'POST':
        role.role_name = request.POST.get('txt_name')
        role.save()
        return redirect('HR:role')
    else:
        return render(request, 'HR/Role.html', {'editrole': role})

def viewemployee(request):
    emp = tbl_employee.objects.all()
    return render(request, 'HR/ViewEmployees.html', {'emp':emp})

def addattendence(request, id):
    attendence = tbl_attendence.objects.filter(employee=id,attendence_date=date.today()).count()
    if attendence > 0:
        return render(request, "HR/ViewEmployees.html",{"msg":"Attendence Add Already"})
    if request.method == "POST":
        tbl_attendence.objects.create(
            employee = tbl_employee.objects.get(id=id),
            attendence_intime = request.POST.get("txt_intime"),
            attendence_outtime = request.POST.get("txt_outtime")
        )
        return render(request, "HR/ViewEmployees.html",{"msg":"Attendence Add Successfully"})
    else:
        return render(request, "HR/Attendence.html",)

def addsalary(request, id):
    dates = date.today()
    salary = tbl_salary.objects.filter(employee=id,salary_date__month=dates.month).count()
    if salary > 0:
        return render(request, "HR/ViewEmployees.html",{"msg":"Salary Add Already"})
    if request.method == "POST":
        tbl_salary.objects.create(
            employee = tbl_employee.objects.get(id=id),
            salary_amount = request.POST.get("txt_salary")
        )
        return render(request, "HR/ViewEmployees.html",{"msg":"Salary Add Successfully"})
    else:
        return render(request, "HR/Salary.html",)

def viewattendence(request):
    emp = tbl_attendence.objects.all()
    if request.method == "POST":
        dates = request.POST.get("txt_date")
        emp = tbl_attendence.objects.filter(attendence_date=dates)
        return render(request, 'HR/View_attendence.html', {'emp':emp})
    return render(request, 'HR/View_attendence.html', {'emp':emp})

def viewsalary(request):
    emp = tbl_salary.objects.all()
    if request.method == "POST":
        dates = request.POST.get("txt_date")
        date_object = datetime.strptime(dates, "%Y-%m")
        emp = tbl_salary.objects.filter(salary_date__month=date_object.month)
        return render(request, 'HR/ViewSalary.html', {'emp':emp})
    return render(request, 'HR/ViewSalary.html', {'emp':emp})

def viewleaverequest(request):
    emp = tbl_leave.objects.all()
    return render(request, 'HR/ViewLeave_request.html', {'emp':emp})

def verifyleave(request, id, status):
    leave = tbl_leave.objects.get(id=id)
    leave.leave_status = status
    leave.save()
    return redirect('HR:viewleaverequest')


def contentpage(request):
    # Fetch all recruitment content for listing
    hr=tbl_hr.objects.get(id=request.session['hrid'])
    contents = tbl_recruitment.objects.all()
    
    if request.method == 'POST':
        # Get form data
        content_text = request.POST.get('txt_content')
        last_date = request.POST.get('txt_lastdate')
        
        # Validate form fields
        if not content_text or not last_date:
            messages.error(request, "Please fill all fields!")
            return redirect('HR:contentpage')
            
        # Check if HR is logged in (session exists)
        if 'hrid' not in request.session:
            messages.error(request, "You must be logged in as HR to add content!")
            return redirect('Guest:login')
        
            hr_id = request.session['hrid']
            hr = tbl_hr.objects.filter(id=hr_id).first()
        
        # Check if HR exists
        if not hr:
            messages.error(request, "HR account not found!")
            return redirect('HR:contentpage')
        
        # Create and save recruitment content
        tbl_recruitment.objects.create(recruitment_content=content_text,recruitment_lastdate=last_date,hr=hr)
        messages.success(request, "Content added successfully!")
        return redirect('HR:contentpage')
    
    # GET request - render the page
    return render(request, 'HR/Recruitment.html', {'contents': contents})

def deletecontent(request, content_id):
    # Check if HR is logged in
    if 'hr_id' not in request.session:
        messages.error(request, "You must be logged in to delete content!")
        return redirect('HR:login')
    
    # Check if content exists
    content = tbl_recruitment.objects.filter(id=content_id).first()
    if not content:
        messages.error(request, "Content not found!")
    else:
        content.delete()
        messages.success(request, "Content deleted successfully!")
    
    return redirect('HR:contentpage')

def viewrequest(request, id):
    req = tbl_request.objects.filter(recruitment=id)
    return render(request,"HR/ViewRequest.html",{"jobs":req,"id":id})

def verifyreqest(request, id, status, reqid):
    req = tbl_request.objects.get(id=id)
    req.request_status = status
    req.save()
    return redirect("HR:viewrequest",reqid)

def deleteemployee(request, id):
    employee = get_object_or_404(tbl_employee, id=id)
    employee.delete()
    return redirect('HR:viewemployee')

def delete_salary(request, id):
    # Use tbl_salary instead of Salary
    salary = get_object_or_404(tbl_salary, id=id)

    # Delete the salary record
    salary.delete()

    # Redirect or render a response
    return redirect('HR:viewsalary')  # Adjust the redirect as necessary

def complaints(request):
    complaint = tbl_complaint.objects.filter(hr=request.session["hrid"])
    if request.method == "POST":
        tbl_complaint.objects.create(complaint_title=request.POST.get("txt_title"),complaint_content=request.POST.get("txt_content"),hr=tbl_hr.objects.get(id=request.session["hrid"]))
        return render(request,"HR/Complaint.html",{"msg":"Complaint Send Sucessfully.."})
    else:
        return render(request,"HR/Complaint.html",{"complaint":complaint})

# HR/views.py
def view_applications(request):
    applications = tbl_request.objects.all().order_by('-request_date')
    return render(request, 'HR/applications.html', {'applications': applications})



