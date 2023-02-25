from django import forms
from admins.models import Admin  

class AdminsForm(forms.ModelForm):  
    class Meta:  
        model=Admin
        fields = "__all__" 