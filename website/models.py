from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
