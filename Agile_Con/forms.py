from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Attendee, CustomerOrder

#from .models import EmployeeAdmin


class AttendeeCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Attendee
        fields = ('attendee_id', 'name', 'user')


class AttendeeChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Attendee
        fields = ('attendee_id', 'name', 'user')

#class CustomUserCreationForm(UserCreationForm):
#    class Meta(UserCreationForm):
#        model = EmployeeAdmin
#        fields = ('username', 'role')

#class CustomUserChangeForm(UserChangeForm):
#    class Meta(UserChangeForm):
#        model = EmployeeAdmin
#        fields = ('username', 'role')


class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ('attendee', 'presentation')