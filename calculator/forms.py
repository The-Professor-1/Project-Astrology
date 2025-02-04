from django import forms
from .models import Message
class Myform(forms.Form):
    your_name = forms.CharField(max_length=50,label='የእርስዎ ስም፡')
    your_mothers_name = forms.CharField(max_length=50,label="የእናትዎ ስም፡")
class Contactus(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','message']