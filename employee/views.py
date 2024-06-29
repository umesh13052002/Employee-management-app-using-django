from django.shortcuts import render,HttpResponse,redirect
from .models import Emp
# Create your views here.
def student_home(request):
    return render(request, 'employee/index.html', {'message': 'Hello!'})
def add_emp(request):
    if request.method == "POST":
        emp_name =request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e=Emp()
        e.emp_name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
            
        e.save()
        
        return redirect("/student/home")
    return render(request, 'employee/add_emp.html',{})
