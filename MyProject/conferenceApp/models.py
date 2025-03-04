from django.db import models
from django.core.validators import ValidationError, MaxValueValidator, FileExtensionValidator, MinValueValidator
import re

# Create your models here.
def validate_title(value):
    if not re.match(r'^[A-Za-z\s]+$', value):
        raise ValidationError('Invalid title')

class Category(models.Model):
    title = models.CharField(max_length=255, validators=[validate_title])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"
    

class Conference(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    price=models.FloatField(validators=[MinValueValidator(limit_value = 0, message="Price must be positive")])
    capacity = models.IntegerField(validators=[MaxValueValidator(limit_value = 1000, message="Capacity cannot exceed 1000"), MinValueValidator(limit_value = 0, message="Capacity must be positive")])
    program = models.FileField(upload_to='files/', validators = [
        FileExtensionValidator(allowed_extensions = ['pdf', 'png', 'jpeg', 'jpg'])
    ])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='conferences')
    
    def __str__(self):
        return self.title
    
    def clean (self):
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be after start date")