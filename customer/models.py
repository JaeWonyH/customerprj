from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birthdate = models.DateField()
    gender = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '('+str(self.id)+')'
