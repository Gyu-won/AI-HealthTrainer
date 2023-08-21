from django import forms
from .models import Exercise
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Goal


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('name', 'description')
        
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

        labels = {
            'username': _('Username'),
            'first_name': _('Nama Depan'),
            'last_name': _('Nama Belakang'),
            'email': _('Email')
        }

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['start', 'stop', 'goal']
        widgets = {
            'start': forms.DateInput(attrs={'type': 'date'}),
            'stop': forms.DateInput(attrs={'type': 'date'}),
        }
        