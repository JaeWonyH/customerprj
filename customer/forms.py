from django import forms
from .models import Customer

#ModelForm을 상속받는 PostModelForm 클래스 정의

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = ('name','email','birthdate','gender')
