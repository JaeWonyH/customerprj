from django import forms
from django.db import models

# name 필드의 length가 2보다 작으면 검증오류 발생시키는 함수
def min_length_2_validator(value):
    if len(value)<2:
        #ValidationError 예외를 강제로 발생
        raise forms.ValidationError('name은 2글자 이상 입력하시요!')

class Customer(models.Model):
    name = models.CharField(max_length=100,validators=[min_length_2_validator])
    email = models.EmailField()
    birthdate = models.DateField()
    gender = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '('+str(self.id)+')'
