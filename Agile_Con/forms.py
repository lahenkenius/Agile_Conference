from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Attendee, CustomerOrder

#from .models import EmployeeAdmin


class AttendeeCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', max_length=50, widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = Attendee
        fields = ('attendee_id', 'name', 'user')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password1

    def save(self, commit=True):
        Attendee = super(UserCreationForm, self).save(commit=False)
        Attendee.password = self.cleaned_data['password1']
        Attendee.save()
        return Attendee


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