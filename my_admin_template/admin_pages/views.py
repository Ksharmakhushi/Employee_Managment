from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
# Create your views here.
def home(request):
    return render(request,"home.html")

def addEmployee(request):
    return render(request,"addEmployee.html")

def viewEmployee(request):
    # return render(request,"viewEmployee.html")
    return redirect('viewAllEmployeeList')

def updateEmployee(request,empid):
    emp = get_object_or_404(Employee,empid =empid)
    if request.method == "POST":
        emp.ename = request.POST.get('ename')
        emp.eemail = request.POST.get('eemail')
        emp.econtact = request.POST.get('econtact')
        emp.ejoindate = request.POST.get('ejoindate')
        emp.esalary = request.POST.get('esalary')
        emp.edept = request.POST.get('edept')
        emp.ecity = request.POST.get('ecity')

        emp.save()
    return render(request,'update.html',{'emp':emp})

def deleteEmployeeRecord(request,empid):
    emp = get_object_or_404(Employee,empid=empid)
    emp.delete()

    return redirect('viewEmployeeList')

def profile(request):
    return render(request,"profile.html")

def saveEmployee(request):
    if(request.method == "POST"):
        eid =  request.POST.get('eid')
        ename = request.POST.get('ename')
        eemail =  request.POST.get('eemail')
        econtact =  request.POST.get('econtact')
        edept =  request.POST.get('edept')
        ejoindate = request.POST.get('ejdate')
        esalary =  request.POST.get('esal')
        ecity =   request.POST.get('ecity')
                                  # (modelname = viewname)
        Employee.objects.create(empid=eid,  ename=ename,eemail=eemail,econtact=econtact,edept=edept,ejoindate=ejoindate,esalary=esalary,ecity=ecity)

        return redirect('viewAllEmployeeList') # create a url for function calling
    return render(request,"addEmployee.html")


def viewAllEmployeeList(request):
    data = Employee.objects.all()
    print(data)

    return render(request,"viewEmployee.html",{'emp_data':data})

def updateEmployeeDetails(request):
    if(request.method == "POST"):
        eid = request.POST.get('eid')
        ename = request.POST.get('ename')
        eemail = request.POST.get('eemail')
        econtact = request.POST.get('econtact')
        edept = request.POST.get('edept')
        ejoindate = request.POST.get('ejdate')
        esalary = request.POST.get('esal')
        ecity = request.POST.get('ecity')

        Employee.objects.filter(empid=eid).update(empid=eid,ename=ename,eemail=eemail,econtact=econtact,edept=edept,ejoindate=ejoindate,esalary=esalary,ecity=ecity)

        return redirect('viewEmployeeList') # create a url