from django.db import models

class CategoryActivity(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title


class ProcedureActivity(models.Model):
    category = models.ForeignKey(CategoryActivity, related_name="procedures", on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, blank=True, null=True) 

    def __str__(self):
        return f"{self.category.title} {self.text[:20]}"
    
    
class Doctors(models.Model):
    specialization = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    about_myself = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='doctors/photos/', blank=True, null=True)
    information = models.TextField(max_length=255)
    image_info = models.ImageField(upload_to='doctors/image/', blank=True, null=True)
    specialty = models.TextField(max_length=255, default="Доктор")
    education = models.TextField(max_length=1000)
    experience = models.TextField(max_length=1000, blank=True, null=True)
    work_method = models.TextField(max_length=1000, blank=True, null=True)
    work_directions = models.TextField(max_length=1000, blank=True, null=True)
    skills = models.TextField(max_length=1000, blank=True, null=True)
    professional_development = models.TextField(max_length=1000, blank=True, null=True)
    additional_professional_activity  = models.TextField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    