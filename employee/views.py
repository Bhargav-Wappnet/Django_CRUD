from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import employee


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/display")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "Home.html", {"form": form})


def display(request):
    employees = employee.objects.all()
    return render(request, "display.html", {"employees": employees})


def edit(request, id):
    employees = employee.objects.get(id=id)
    return render(request, "edit.html", {"employee": employees})


def update(request, id):
    employees = employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employees)
    if form.is_valid():
        form.save()
        return redirect("/display")
    return render(request, "display.html", {"employee": employees})


def destroy(request, id):
    employees = employee.objects.get(id=id)
    employees.delete()
    return redirect("/display")
