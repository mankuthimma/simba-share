from django.db import models

class Share(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    path = models.CharField(max_length=100)
    valid_users = models.CharField(max_length=100)


