from django.db import models
from django.utils import timezone
# Create your models here.
class Users_info(models.Model):
  phone_email = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  date_added = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return f"Phone: {self.phone_email} - Password: {self.password}"