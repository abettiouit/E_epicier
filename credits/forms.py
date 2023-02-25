from django import forms
from credits.models import Credit  

class CreditForm(forms.ModelForm):  
    class Meta:  
        model=Credit
        #fields=['quantite','product','client','price','total']
        fields = "__all__" 