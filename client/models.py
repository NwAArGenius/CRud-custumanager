from django.db import models

# Create your models here.
class Client(models.Model):
    Status = [
        ('is_active', 'is_active'),
        ('is_not_active', 'is_not_active')
    ]
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=9)
    status = models.CharField(max_length=23, choices=Status, blank=True)
    
    def __str__(self):
        return self.full_name