from django import forms
from .models import student

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"
        widgets={
            'dateNaissance':forms.DateInput(attrs={'type':'date'}),
            'genre' :forms.RadioSelect(choices=student.GENDER_CHOICES),
        }