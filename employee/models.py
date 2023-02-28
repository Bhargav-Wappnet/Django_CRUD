from django.db import models


# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    join_date = models.models.DateField(auto_now_add=True)

    class Meta:
        db_table = "employee"