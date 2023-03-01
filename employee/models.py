from django.db import models


# Create your models here.
class employee(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)

    class Meta:
        db_table = "employee"
