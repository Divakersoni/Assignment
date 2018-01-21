from django.db import models

class create_assignment(models.Model):
    name = models.CharField(max_length=100,unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True)
    deadline = models.DateField()

    def __str__(self):
        return self.name