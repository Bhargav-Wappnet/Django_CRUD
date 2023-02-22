from django.db import models


# In This Class Used The Primary Key and Verbose Name As an argument.
# And Also use Email Field with Unique argument And Datefield.
class Employe(models.Model):
    EmployeID = models.AutoField(auto_created=True, primary_key=True,
                                 verbose_name="EmpID")
    Name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    Email = models.EmailField(unique=True, max_length=254)
    JoiningDate = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# In this class impement the foreignkey plus protect attribute.
class Developer(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.PROTECT)
    Technology = models.CharField(max_length=50)
    DefaultSalary = models.IntegerField(default=25000)


# In this class impement the foreignkey plus cascade attribute.
class Designer(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    Technology = models.CharField(max_length=50)
    DefaultSalary = models.IntegerField(default=20000)


# In this class impement the foreignkey plus set null attribute.
class BussinesAnalyst(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    Tool = models.CharField(max_length=50)
    DefaultSalary = models.IntegerField(default=15000)
