from django.db import models

# Create your models here.
class Company(models.Model):
    advocates = models.ManyToManyField('Advocate', blank=True, related_name="companys")
    name = models.CharField(max_length=50, blank=True)
    logo = models.ImageField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    href = models.URLField(blank=True, null=True)
   
    def __str__(self):
        return self.name
    
    

class Advocate(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(blank=True, null=True)
    short_bio = models.TextField(max_length=255, blank=True, null=True)
    long_bio = models.TextField(blank=True, null=True)
    advocate_years_exp = models.PositiveIntegerField(default=1)
    links = models.JSONField(blank=True)
    
    def __str__(self):
        return self.name
    
