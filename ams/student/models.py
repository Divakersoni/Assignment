from django.db import models
import django
from create.models import create_assignment
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100, unique= True)
    agn_file = models.FileField()
    assignment = models.ForeignKey(create_assignment, on_delete=models.CASCADE)
    date = models.DateField('Date', auto_now=True)

    def __str__(self):
        return self.name