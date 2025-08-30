from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q


def index(request):
    return render(request, "index.html")


def all_emp(request):
    emps = Employee.objects.all()
    return render(request, "view_all_emp.html", {"emps": emps})


from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        salary = int(request.POST["salary"])
        bonus = int(request.POST["bonus"])
        phone = request.POST["phone"]
        loc = request.POST["loc"]  # ✅ Location Field
        dept_id = request.POST["dept"]
        role_id = request.POST["role"]

        new_emp = Employee(
            first_name=first_name, last_name=last_name, salary=salary,
            bonus=bonus, phone=phone, loc=loc,  # ✅ Location Save
            dept_id=dept_id, role_id=role_id, hire_date=datetime.today()  # ✅ Hire Date
        )
        new_emp.save()
        return HttpResponse("Employee Added Successfully!")

    elif request.method == "GET":
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, "add_emp.html", {"departments": departments, "roles": roles})

    else:
        return HttpResponse("An Exception Occurred! Employee Not Added...")


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_remove = Employee.objects.get(id=emp_id)  # ✅ `pbjects` → `objects`
            emp_to_be_remove.delete()
            return HttpResponse("Employee Removed Successfully...")
        except:
            return HttpResponse("Please Enter A Valid EMP ID...")

    emps = Employee.objects.all()
    context = {"emps": emps}
    return render(request, "remove_emp.html", context)


def filter_emp(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        dept = request.POST.get("dept", "").strip()
        role = request.POST.get("role", "").strip()

        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        if dept:
            emps = emps.filter(dept_id__icontains=dept)

        if role:
            emps = emps.filter(role_id__icontains=role)

        context = {
            "emps": emps,
            "departments": Department.objects.all(),
            "roles": Role.objects.all(),
        }
        return render(request, "view_all_emp.html", context)

    elif request.method == "GET":
        context = {
            "departments": Department.objects.all(),
            "roles": Role.objects.all(),
        }
        return render(request, "filter_emp.html", context)

    else:
        return HttpResponse("An Exception Occurred!")