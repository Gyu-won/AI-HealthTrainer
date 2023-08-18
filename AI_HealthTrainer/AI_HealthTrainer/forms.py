from django import forms
from .models import Exercise
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import goal


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name']
        
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class GoalForm(forms.ModelForm):
    class Meta:
        model = goal
        fields = ['id','start', 'stop','goal','user']