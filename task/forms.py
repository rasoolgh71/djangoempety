from django import forms
from django.core.validators import MaxLengthValidator,MinLengthValidator
class Emailform(forms.Form):
    subject=forms.CharField(max_length=100,required=False)
    email=forms.CharField(max_length=30,required=False)
    message=forms.CharField(max_length=200)
    #number=forms.IntegerField(
       # [MinLengthValidator(10),MaxLengthValidator(1000)],
   # )