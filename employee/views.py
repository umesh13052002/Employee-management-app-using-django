from django.shortcuts import render,HttpResponse

# Create your views here.
def student_home(request):
    return render(request, 'employee/index.html', {'message': 'Hello!'})
def add_emp(request):
    return render(request, 'employee/add_emp.html',{})