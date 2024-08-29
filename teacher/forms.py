from django import forms
from .models import teacher

class teacherForM(forms.ModelForm):
    class Meta:
        model = teacher
        fields = "__all__"
        widgets={
            'dateNaissance':forms.DateInput(attrs={'type':'date'}),
            'genre' :forms.RadioSelect(choices=teacher.GENDER_CHOICES),
        }