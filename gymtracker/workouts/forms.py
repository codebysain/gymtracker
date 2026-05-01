from django import forms
from .models import Workout, Set

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['exercise', 'reps', 'weight']