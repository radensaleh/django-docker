from django.urls import path,include
from . import views

urlpatterns = [
    #karyawan
    path('', views.employee_form,name='employee_insert'), # get and post req. for insert operation
    path('<int:id>/', views.employee_form,name='employee_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list'), # get req. to retrieve and display all records
    #posisi
    path('posisi/',views.employee_position,name="employee_position"),
    path('deletePosition/<int:id>/', views.position_delete, name='position_delete'),
]
