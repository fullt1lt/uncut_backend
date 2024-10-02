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