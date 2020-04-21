from django.shortcuts import render, redirect
from .forms import EmployeeForm, PositionForm
from .models import Employee, Position

# Create your views here.


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')


def employee_position(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PositionForm()
        else:
            posisi = Position.objects.get(pk=id)
            form = PositionForm(instance=posisi)
        context = Position.objects.all()
        return render(request, "employee_register/employee_position.html", {'form': form, 'position_list': context})
    else:
        if id == 0:
            form = PositionForm(request.POST)
        else:
            posisi = Position.objects.get(pk=id)
            form = PositionForm(request.POST, instance=posisi)
        if form.is_valid():
            form.save()
        return redirect('/posisi')


def position_delete(request, id):
    posisi = Position.objects.get(pk=id)
    posisi.delete()
    return redirect('/posisi')
