from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    phone = models.CharField(max_length=15)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    loc = models.CharField(max_length=100, default="Not Provided")  # ✅ Location Field
    hire_date = models.DateField(auto_now_add=True)  # ✅ Hire Date (Auto Set)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
