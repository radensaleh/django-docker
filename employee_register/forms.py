from django import forms
from .models import Employee, Position


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = {
            'fullname': 'Nama Lengkap',
            'emp_code': 'Kode Karyawan',
            'mobile': 'Nomor Telepon/HP',
            'position': 'Posisi'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Pilih"
        self.fields['emp_code'].required = False


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('title',)
        labels = {'title': 'Posisi'}

    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
