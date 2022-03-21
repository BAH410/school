from django import forms
from .models import Register_Student


class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = Register_Student
        fields = ['fname', 'lname', 'email', 'dob',
                  'edu_level', 'home_address', 'next_of_kin']
